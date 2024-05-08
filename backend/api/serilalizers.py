
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta: #info accept and return for each user
        model = User
        fields = ["id", "username", "password"]
        #take pws when new user, don't show pw when getting info about user
        extra_kwargs = {"password": {"write_only": True}}