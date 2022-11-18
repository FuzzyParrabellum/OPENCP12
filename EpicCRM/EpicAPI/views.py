from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from EpicAPI.models import EpicTeamMember, Client, Contract, Event
from EpicAPI.serializers import EpicTeamMemberListSerializer, \
    EpicTeamMemberDetailSerializer, ClientListSerializer, ClientDetailSerializer,\
    ContractListSerializer, ContractDetailSerializer, EventListSerializer,\
    EventDetailSerializer
from EpicAPI.permissions import IsManagerOrAdmin, IsContact



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

    def __str__(self):
        return "EpicTeamMemberViewset"

class ClientViewset(ModelViewSet, ListOrDetailMixin):

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'create']:
            self.permission_classes = [IsAuthenticated, IsContact]
        elif self.action in ['retrieve', 'list']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(ClientViewset, self).get_permissions()

    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer

    def get_queryset(self):
        return Client.objects.all()

    def __str__(self):
        return "ClientViewset"

class ContractViewset(ModelViewSet, ListOrDetailMixin):

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'create']:
            self.permission_classes = [IsAuthenticated, IsContact]
        elif self.action in ['retrieve', 'list']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(ContractViewset, self).get_permissions()

    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer

    def get_queryset(self):
        return Contract.objects.all()

    def __str__(self):
        return "ContractViewset"

class EventViewset(ModelViewSet, ListOrDetailMixin):

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'create']:
            self.permission_classes = [IsAuthenticated, IsContact]
        elif self.action in ['retrieve', 'list']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super(EventViewset, self).get_permissions()

    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer

    def get_queryset(self):
        return Event.objects.all()

    def __str__(self):
        return "EventViewset"

