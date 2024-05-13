from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serilalizers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    
    queryset = User.objects.all() #make sure we don't make new user
    serializer_class = UserSerializer #what is accaptable to make new user class
    permission_classes = [AllowAny] #allows non auths to create new user
