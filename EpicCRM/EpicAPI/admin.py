from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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

class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_fullname', 'sales_contact', 'status', 'payment_due')
    list_filter = ('status',)
    search_fields = ("client__last_name__istartswith", )

    def client_fullname(self, obj):
        return f"{obj.client.last_name} {obj.client.first_name}"

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_fullname', 'support_contact', 'event_date','event_status')
    list_filter = ('event_status',)
    search_fields = ("client__last_name__istartswith", )

    def client_fullname(self, obj):
        return f"{obj.client.last_name} {obj.client.first_name}"

class EpicTeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'username', 'email')
    list_filter = ('role',)
    # ordering = ["username"]
    fields = ("username", "password", "first_name", "last_name", "email", "role")
    search_fields = ("id", "username")
    # def save_model(self, request, obj, form, change):
    #     obj = form.save(commit=False)
    #     obj.is_staff = True
    #     obj.save()


admin.site.register(EpicTeamMember, EpicTeamMemberAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
