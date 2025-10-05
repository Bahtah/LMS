from rest_framework import permissions


class HasRole(permissions.BasePermission):
    role_name = None

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.roles.filter(name=self.role_name).exists()

class IsAdmin(HasRole):
    role_name = "ADMIN"

class IsInstructor(HasRole):
    role_name = "INSTRUCTOR"

class IsStudent(HasRole):
    role_name = "STUDENT"
