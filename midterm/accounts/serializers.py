
from rest_framework import serializers
from .models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class CustomUserSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(write_only=True)
    middle_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    phone_number = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'middle_name', 'last_name', 'password', 'confirm_password',
                  'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User.objects.create_user(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            password=self.validated_data['password'],
            middle_name=self.validated_data['middle_name'],
            phone_number=self.validated_data['phone_number'],

        )
        confirm_password = self.validated_data['confirm_password'],
        user.is_active = False
        user.save()

        return user
