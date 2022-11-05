from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from EpicAPI.models import EpicTeamMember, Client, Contract, Event
from EpicAPI.serializers import EpicTeamMemberSerializer, ClientSerializer,\
                            ContractSerializer, EventSerializer
# Create your views here.

class EpicTeamMemberViewset(ModelViewSet):

    serializer_class = EpicTeamMemberSerializer

    def get_queryset(self):
        return EpicTeamMember.objects.all()

class ClientViewset(ModelViewSet):

    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()

class ContractViewset(ModelViewSet):

    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()

class EventViewset(ModelViewSet):

    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()

