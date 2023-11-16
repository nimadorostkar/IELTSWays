from rest_framework.views import APIView
from ..functions import validate_token
from config import responses


class UserValidationView(APIView):
    def get(self, request):
        cookie = request.COOKIES.get('HTTP_ACCESS')
        if cookie is None:
            return responses.bad_request(errors={"User is not logged in"})
        access_token = cookie.split(' ')[1]
        if validate_token(access_token):
            return responses.ok(data={"is_valid": "True"})
        else:
            return responses.unauthorized(errors={"is_valid": "False"})
