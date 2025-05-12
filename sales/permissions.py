from rest_framework.permissions import BasePermission

class IsSlaesOrAdminUser(BasePermission):
    """
    Custom permission to only allow sales or admin users to access the view.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and is either a sales or admin user
        return request.user and (request.user.is_staff or request.user.groups.filter(name='Vendores').exists())
    
class IsCustomerOrAdminUser(BasePermission):
    """
    Custom permission to only allow customer or admin users to access the view.
    """
    def has_permission(self, request, view, obj):
        # Check if the user is authenticated and is either a customer or admin user
        if request.user.is_staff:
            return True
        return obj.customer.id == request.user.id