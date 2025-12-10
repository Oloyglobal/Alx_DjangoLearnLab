from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import authenticate


from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


# Register view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token, _ = Token.objects.get_or_create(user=user)
        response.data['token'] = token.key
        return response

# Login view
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=400)

# Profile view
class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user





@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if user_to_follow == request.user:
        return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    request.user.following.add(user_to_follow)
    return Response({"message": f"You are now following {user_to_follow.username}."})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({"message": f"You have unfollowed {user_to_unfollow.username}."})
