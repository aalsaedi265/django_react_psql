
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta: #info accept and return for each user
        model = User
        fields = ["id", "username", "password"]
        #take pws when new user, don't show pw when getting info about user
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self,validated_data ):
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author":{"read_only":True}}