from rest_framework.serializers import ModelSerializer

from EpicAPI.models import EpicTeamMember, Client, Contract, Event


class EpicTeamMemberListSerializer(ModelSerializer):

    class Meta:
        model = EpicTeamMember
        fields = ['id', 'username', 'first_name', 'last_name', 'role']

class EpicTeamMemberDetailSerializer(ModelSerializer):

    class Meta:
        model = EpicTeamMember
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email',\
             'role']

class ClientListSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'sales_contact',\
            'existing_client']

class ClientDetailSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'mobile', \
            'company_name', 'date_created', 'date_updated', 'sales_contact',\
            'existing_client']

class ContractListSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ['sales_contact', 'client','status', 'amount', 'payment_due']

class ContractDetailSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ['sales_contact', 'client', 'date_created', 'date_updated',\
            'status', 'amount', 'payment_due']

class EventListSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields= ['client', 'contract', 'support_contact', 'event_status', \
            'event_date']

class EventDetailSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields= ['client', 'contract', 'date_created', 'date_updated',\
            'support_contact', 'event_status', 'attendees', 'event_date', 'notes']



# class EpicTeamMemberSerializer(ModelSerializer):

#     class Meta:
#         model = EpicTeamMember
#         fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email',\
#              'role']

# class ClientSerializer(ModelSerializer):

#     class Meta:
#         model = Client
#         fields = ['first_name', 'last_name', 'email', 'phone', 'mobile', \
#             'company_name', 'date_created', 'date_updated', 'sales_contact',\
#             'existing_client']

# class ContractSerializer(ModelSerializer):

#     class Meta:
#         model = Contract
#         fields = ['sales_contact', 'client', 'date_created', 'date_updated',\
#             'status', 'amount', 'payment_due']

# class EventSerializer(ModelSerializer):

#     class Meta:
#         model = Event
#         fields= ['client', 'contract', 'date_created', 'date_updated',\
#             'support_contact', 'event_status', 'attendees', 'event_date', 'notes']