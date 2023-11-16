from django.db import transaction
from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserSerializer


class UserRegister(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    @transaction.atomic
    def patch(self, *args, **kwargs):
        data = self.request.data
        serializer = RegisterSerializer(user, data=data, partial=True)
        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "errors": [_("incorrect data"), serializer.errors],
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save()
        user.name = data["name"]
        #user.username = data["username"]
        user.save()
        user.refresh_from_db()
        user_data = UserSerializer(user).data
        user.save()
        return Response(
            {
                "success": True,
                "data": {"user_data": user_data},
            },
            status=status.HTTP_200_OK,
        )

