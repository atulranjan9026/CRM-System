from rest_framework import serializers
from .models import Workspace
from apps.users.serializers import UserSerializer

class WorkspaceSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Workspace
        fields = ['id', 'name', 'description', 'created_by', 'members', 'created_at', 'updated_at']
