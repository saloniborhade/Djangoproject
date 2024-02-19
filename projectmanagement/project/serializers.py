# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']

class ProjectSerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    client = ClientSerializer(read_only=True)
    # users = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']