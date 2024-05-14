
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serilalizers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here

class NoteListCreate(generics.ListCreateAPIView):
    #will list all created node or create a node
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
         #for all node, super waist of electricity do this Note.objects.all()
         #below is my specific author
        return Note.objects.filter(author = user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author = self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)
    

class CreateUserView(generics.CreateAPIView):
    
    queryset = User.objects.all() #make sure we don't make new user
    serializer_class = UserSerializer #what is accaptable to make new user class
    permission_classes = [AllowAny] #allows non auths to create new user
    