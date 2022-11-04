from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
from EpicAPI.models import EpicTeamMember, Contract, Event, Client

admin.site.site_header  =  "Epic Event CRM"  
admin.site.site_title  =  "Epic Event CRM"
admin.site.index_title  =  "Lists of Clients, Contracts and Events currently in CRM"

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name','first_name','company_name', 'sales_contact', 
                    'existing_client')
    list_filter = ('existing_client',)

    # istartswith for case insensitive search
    search_fields = ("last_name__istartswith", )

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.role == 'MANAGER':
            return True
        if obj != None:
            # The object is None with a view list, not with a detail view
            return request.user == obj.sales_contact
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.role == 'MANAGER':
            return True
        if obj != None:
            # The object is None with a view list, not with a detail view
            return request.user == obj.sales_contact
        else:
            return False

class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_fullname', 'sales_contact', 'status', 'payment_due')
    list_filter = ('status',)
    search_fields = ("client__last_name__istartswith", )

    def client_fullname(self, obj):
        return f"{obj.client.last_name} {obj.client.first_name}"

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.role == 'MANAGER':
            return True
        if obj != None:
            # The object is None with a view list, not with a detail view
            return request.user == obj.sales_contact
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.role == 'MANAGER':
            return True
        if obj != None:
            # The object is None with a view list, not with a detail view
            return request.user == obj.sales_contact
        else:
            return False

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_fullname', 'support_contact', 'event_date','event_status')
    list_filter = ('event_status',)
    search_fields = ("client__last_name__istartswith", )

    def client_fullname(self, obj):
        return f"{obj.client.last_name} {obj.client.first_name}"

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.role == 'MANAGER':
            return True
        if obj != None:
            # The object is None with a view list, not with a detail view
            return request.user == obj.client.sales_contact or \
                request.user == obj.support_contact
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.role == 'MANAGER':
            return True
        if obj != None:
            # The object is None with a view list, not with a detail view
            return request.user == obj.client.sales_contact or \
                request.user == obj.support_contact
        else:
            return False

class EpicTeamMemberAdmin(UserAdmin):
    list_display = ('id', 'role', 'username', 'email')
    list_filter = ('role',)
    # ordering = ["username"]
    fieldsets = (
        ('Required', {'fields':("username", "password", "role")}), 
        ('Personal info', {'fields':("first_name", "last_name", "email")}),
         )
    search_fields = ("id", "username")
    # def save_model(self, request, obj, form, change):
    #     obj = form.save(commit=False)
    #     obj.is_staff = True
    #     obj.save()

admin.site.register(EpicTeamMember, EpicTeamMemberAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
