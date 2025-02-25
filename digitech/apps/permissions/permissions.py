from rest_framework.permissions import BasePermission

class CanViewProject(BasePermission):
    def has_permission(self, request, view):
        # Custom logic to check if the user can view the project
        return request.user and request.user.is_authenticated

class CanEditTask(BasePermission):
    def has_permission(self, request, view):
        # Custom logic to check if the user can edit the task
        return request.user and request.user.is_authenticated and request.user.has_perm('tasks.change_task')
