from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser

class IsManagerOrAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.role == 'MANAGER':
            return True
        return False

class IsContact(BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser or request.user.role == 'MANAGER':
            return True

        elif view.__str__() == "ClientViewset":
            # Check if user is client's sales_contact, or superuser or manager
            return request.user == obj.sales_contact

        elif view.__str__() == "ContractViewset":
            return request.user == obj.sales_contact or\
                request.user == obj.client.sales_contact


        elif view.__str__() == "EventViewset":
            return request.user == obj.support_contact or\
                request.user == obj.client.sales_contact

        else:
            return False