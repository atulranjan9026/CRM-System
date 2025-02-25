from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Workspace
from .serializers import WorkspaceSerializer
from apps.permissions.permissions import CanViewProject, CanEditTask

class WorkspaceViewSet(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
    # permission_classes = [IsAuthenticated, CanViewProject, CanEditTask]
