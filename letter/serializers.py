from rest_framework import serializers
from letter.models import Letter
from accounts.serializers import UserSerializer

class LetterSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Letter
        fields = '__all__'



class CreateLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'