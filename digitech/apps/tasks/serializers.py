from rest_framework import serializers
from .models import Task
from apps.users.serializers import UserSerializer
from apps.projects.serializers import ProjectSerializer

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
