from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from EpicAPI.models import EpicTeamMember, Client, Contract, Event
from EpicAPI.serializers import EpicTeamMemberSerializer, ClientSerializer,\
                            ContractSerializer, EventSerializer
# Create your views here.

class EpicTeamMemberAPIView(APIView):

    def get(self, *args, **kwargs):
        epic_members = EpicTeamMember.objects.all()
        serializer = EpicTeamMemberSerializer(epic_members, many=True)
        return Response(serializer.data)

class ClientAPIView(APIView):

    def get(self, *args, **kwargs):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

class ContractAPIView(APIView):

    def get(self, *args, **kwargs):
        contracts = Contract.objects.all()
        serializer = ContractSerializer(contracts, many=True)
        return Response(serializer.data)

class EventAPIView(APIView):

    def get(self, *args, **kwargs):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)