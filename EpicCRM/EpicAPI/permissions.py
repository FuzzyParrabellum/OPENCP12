from rest_framework.permissions import BasePermission


class IsManagerOrAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.role == 'MANAGER':
            return True
        return False