from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class OverView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        serializer = UserSerializer(self.request.user)
        return Response({"success": True,"data": serializer.data,},status=status.HTTP_200_OK)