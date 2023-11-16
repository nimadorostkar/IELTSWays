from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
import re
from django.utils.translation import gettext as _
from rest_framework.throttling import AnonRateThrottle
from accounts.models import User
from config import responses
from accounts.functions import login
from accounts.selectors import get_user
from accounts.serializers import UserSerializer



phone_number_regex = re.compile(r"^09\d{9}")




class AdminOverView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        user=self.request.user

        if user.user_type == "normal":
            return Response("Normal users do not have permission to use this method.", status=status.HTTP_406_NOT_ACCEPTABLE)

        factors = Invoice.objects.filter(status="پرداخت نشده").order_by('-created_at')[:3]
        letters = Letter.objects.all().order_by('-created_at')[:3]

        data = {
            "user_id": user.id,
            "name": user.name,
            "user_type": user.user_type,
            "phone_number": user.phone_number,
            "factors": InvoiceSerializer(factors,many=True).data,
            "letters": LetterSerializer(letters,many=True).data,
        }

        return Response({"success": True,"data": data,},status=status.HTTP_200_OK)


class UsersCountView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        user = self.request.user

        if user.user_type == "normal":
            return Response("Normal users do not have permission to use this method.",status=status.HTTP_406_NOT_ACCEPTABLE)

        users = User.objects.all()

        data = {
            "alluser": users.count(),
            "admin": users.filter(user_type="admin").count(),
            "normal": users.filter(user_type="normal").count(),
            "staff": users.filter(user_type="staff").count(),
        }
        return Response({"success": True, "data": data, }, status=status.HTTP_200_OK)



class InvoicesCountView(APIView):
    #serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        user = self.request.user

        if user.user_type == "normal":
            return Response("Normal users do not have permission to use this method.",status=status.HTTP_406_NOT_ACCEPTABLE)

        invoices = Invoice.objects.all()

        data = {
            "all": invoices.count(),
            "success": invoices.filter(status="پرداخت شده").count(),
            "faild": invoices.filter(status="پرداخت نشده").count(),
        }
        return Response({"success": True, "data": data, }, status=status.HTTP_200_OK)
