from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class Withdraw(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        user = self.request.user
        user.withdraw = True
        user.save()
        return Response('Cancellation was successful', status=status.HTTP_200_OK)
