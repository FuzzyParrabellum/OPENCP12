from rest_framework.serializers import ModelSerializer

from EpicAPI.models import EpicTeamMember, Client, Contract, Event


class EpicTeamMemberSerializer(ModelSerializer):

    class Meta:
        model = EpicTeamMember
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email',\
             'role']

class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'mobile', \
            'company_name', 'date_created', 'date_updated', 'sales_contact',\
            'existing_client']

class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ['sales_contact', 'client', 'date_created', 'date_updated',\
            'status', 'amount', 'payment_due']

class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields= ['client', 'contract', 'date_created', 'date_updated',\
            'support_contact', 'event_status', 'attendees', 'event_date', 'notes']