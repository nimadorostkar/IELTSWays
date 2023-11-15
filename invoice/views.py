from invoice.models import Invoice
from invoice.serializers import InvoiceSerializer, InvoiceEditSerializer, InvoiceCreateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.views.permissions import IsAdmin, IsStaff
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework import pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import GenericAPIView


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class InvoiceView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', 'created_at', 'due_date', 'status']
    search_fields = ['invoice_id', 'description']
    ordering_fields = ['invoice_id', 'created_at', 'due_date', 'price']

    def get(self, *args, **kwargs):

        if self.request.GET.get('created_date_start'):
            start_date = self.request.GET.get('created_date_start')
        else:
            start_date = "2000-1-1"

        if self.request.GET.get('created_date_end'):
            end_date = self.request.GET.get('created_date_end')
        else:
            end_date = "3000-1-1"

        if self.request.user.user_type == "normal":
            user_invoices = Invoice.objects.filter(user=self.request.user)
        else:
            user_invoices = Invoice.objects.all()

        invoices = self.filter_queryset(user_invoices.filter(created_at__range=(start_date,end_date)).distinct())
        page = self.paginate_queryset(invoices)
        if page is not None:
            serializer = InvoiceSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        if self.request.user.user_type == "normal":
            return Response("Normal users do not have permission to use this method.", status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = InvoiceCreateSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            invoice=Invoice.objects.get(id=serializer.data['id'])
            invoice.user = User.objects.get(id=self.request.data['user'])
            invoice.sender=self.request.user
            invoice.save()
            res_serializer = InvoiceSerializer(invoice)
            return Response(res_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



class InvoiceItem(APIView):
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        try:
            invoice = Invoice.objects.get(id=self.kwargs["id"])
            serializer = self.serializer_class(invoice)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("invoice not found or something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)




    def patch(self, request, *args, **kwargs):
        try:
            invoice = Invoice.objects.get(id=self.kwargs["id"])
            serializer = InvoiceEditSerializer(invoice, data=request.data)
            if serializer.is_valid():
                serializer.save()
                invoice.sender = request.user
                invoice.user = User.objects.get(id=request.data['user'])
                invoice.save()
                res_serializer = InvoiceSerializer(invoice)
                return Response(res_serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Invoice not found or something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, *args, **kwargs):
        try:
            invoice = Invoice.objects.get(id=self.kwargs["id"])
            invoice.delete()
            return Response("Invoice deleted", status=status.HTTP_200_OK)
        except:
            return Response("Something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)

