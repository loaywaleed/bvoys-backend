from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserCreate(generics.CreateAPIView):
    """
    A view for creating a new User object.

    post:
    Create a new user instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'firstName' : user.first_name,
            'lastName': user.last_name,
            'username': user.username,
        })