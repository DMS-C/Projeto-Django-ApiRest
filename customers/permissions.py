from rest_framework.permissions import BasePermission

class IsCustomerOrAdmin(BasePermission):
    """
    Custom permission to only allow customers or admins to access the view.
    """
    def has_Object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        return obj.id == request.user.id