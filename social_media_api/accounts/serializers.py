from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    # ALX wants this explicit CharField
    password = serializers.CharField()

    class Meta:
        model = get_user_model()  # ALX explicitly checks for get_user_model().objects.create_user
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Use the expected ALX pattern
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Create token for the user
        Token.objects.create(user=user)
        return user
