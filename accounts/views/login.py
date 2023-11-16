from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.functions import login
from config.settings import ACCESS_TTL
from accounts.serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserLogin(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, *args, **kwargs):
        national_id = self.request.data.get("national_id")
        password = self.request.data.get("password")
        user = authenticate(national_id=national_id, password=password)
        if user is not None:
            access, refresh = login(user)
            data = {
                "refresh_token": refresh,
                "access_token": access,
                "user_data": UserSerializer(user).data}
            response = Response( {"success": True, "data": data}, status=status.HTTP_200_OK)
            response.set_cookie(
                "HTTP_ACCESS",
                f"Bearer {access}",
                max_age=ACCESS_TTL * 24 * 3600,
                secure=True,
                httponly=True,
                samesite="None",
            )
            return response

        else:
            return Response({"success": False, "errors": [_("National-ID or password is incorrect")]},status=status.HTTP_400_BAD_REQUEST)
