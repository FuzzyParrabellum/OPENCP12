from django.shortcuts import render


# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from EpicAPI.models import EpicTeamMember, Client, Contract, Event
from EpicAPI.serializers import EpicTeamMemberListSerializer, \
    EpicTeamMemberDetailSerializer, ClientListSerializer, ClientDetailSerializer,\
    ContractListSerializer, ContractDetailSerializer, EventListSerializer,\
    EventDetailSerializer
from EpicAPI.permissions import IsManagerOrAdmin
# Create your views here.

# Mixin to get List or DetailView for each viewset
# A IMPLEMANTER
class ListOrDetailMixin():

    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'destroy']:
            return self.detail_serializer_class
        else:
            return super().get_serializer_class()


class EpicTeamMemberViewset(ModelViewSet, ListOrDetailMixin):

    permission_classes = [IsAuthenticated, IsManagerOrAdmin]

    serializer_class = EpicTeamMemberListSerializer
    detail_serializer_class = EpicTeamMemberDetailSerializer

    def get_queryset(self):
        return EpicTeamMember.objects.all()

class ClientViewset(ModelViewSet, ListOrDetailMixin):

    permission_classes = [IsAuthenticated]

    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer

    def get_queryset(self):
        return Client.objects.all()

class ContractViewset(ModelViewSet, ListOrDetailMixin):

    permission_classes = [IsAuthenticated]

    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer

    def get_queryset(self):
        return Contract.objects.all()

class EventViewset(ModelViewSet, ListOrDetailMixin):

    permission_classes = [IsAuthenticated]

    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer

    def get_queryset(self):
        return Event.objects.all()

