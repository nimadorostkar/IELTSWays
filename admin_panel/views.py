from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from accounts.models import User
from accounts.serializers import UserSerializer
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework import pagination
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import GenericAPIView

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class RegUserView(GenericAPIView):
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['created_at', 'withdraw']
    search_fields = ['first_name', 'last_name', 'national_id']
    ordering_fields = ['created_at',]

    def get(self, *args, **kwargs):
        users = self.filter_queryset(User.objects.all()).distinct()
        page = self.paginate_queryset(users)
        if page is not None:
            serializer = UserSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RemoveUserView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, *args, **kwargs):
        try:
            user = User.objects.get(id=self.kwargs["id"])
            user.delete()
            return Response("User removed successfully.", status=status.HTTP_200_OK)

        except:
            return Response("User not found or something went wrong, try again.", status=status.HTTP_400_BAD_REQUEST)
