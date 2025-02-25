from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkspaceViewSet

router = DefaultRouter()
router.register(r'workspaces', WorkspaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
