from letter.models import Letter
from letter.serializers import LetterSerializer, CreateLetterSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework import pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import GenericAPIView


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



class LetterView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    serializer_class = LetterSerializer
    queryset = Letter.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', 'created_at']
    search_fields = ['letter_id', 'title', 'body']
    ordering_fields = ['letter_id', 'created_at']

    def get(self, *args, **kwargs):
        if self.request.user.user_type == "normal":
            user_letters = Letter.objects.filter(user=self.request.user)
        else:
            user_letters = Letter.objects.all()
        letters = self.filter_queryset(user_letters.distinct())
        page = self.paginate_queryset(letters)
        if page is not None:
            serializer = LetterSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = LetterSerializer(letters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        if self.request.user.user_type == "normal":
            return Response("Normal users do not have permission to use this method.", status=status.HTTP_406_NOT_ACCEPTABLE)

        print(self.request.user.user_type)
        serializer = CreateLetterSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



class LetterItem(APIView):
    serializer_class = LetterSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        try:
            letter = Letter.objects.get(id=self.kwargs["id"])
            serializer = self.serializer_class(letter)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("Letter not found or something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)




    def patch(self, request, *args, **kwargs):
        try:
            letter = Letter.objects.get(id=self.kwargs["id"])
            serializer = LetterSerializer(letter, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Letter not found or something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, *args, **kwargs):
        try:
            letter = Letter.objects.get(id=self.kwargs["id"])
            letter.delete()
            return Response("Letter deleted", status=status.HTTP_200_OK)
        except:
            return Response("Something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)


