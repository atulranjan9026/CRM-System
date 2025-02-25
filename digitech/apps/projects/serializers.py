from rest_framework import serializers
from .models import Project
from apps.users.serializers import UserSerializer
from apps.workspaces.serializers import WorkspaceSerializer

class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    workspace = WorkspaceSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
