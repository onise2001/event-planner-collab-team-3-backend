from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import  Event, RSVP, Invitation, EventInfo
from .serializers import EventSerializer, RSVPSerializer, InvitationSerializer, EventInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOrganizer

# Create your views here.


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    # def create(self,request):
    #     ...

    def get_permissions(self):
        if self.action in ['list', "retrieve",'head','options']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsOrganizer]

        return [permission() for permission in permission_classes]


class RSVPViewSet(ModelViewSet):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer
    
    
    def perform_create(self, serializer):
        event = serializer.validated_data['event']
        event_info = EventInfo.objects.filter(event=event).first()
        user = self.request.user

        invitation = Invitation.objects.filter(event=event, guest=user).first()
        
        rsvp = serializer.save(user=user)
        event_info.total_rsvps += 1
        
        if invitation:
            if rsvp.accepted:
                event_info.total_accepted_rsvps += 1
                event_info.invitaion_accepted_rsvps += 1
            else :
                event_info.total_rejected_rsvps += 1
                event_info.invitation_rejected_rsvps += 1
        else:
            event_info.total_accepted_rsvps += 1
        
        event_info.save()


        if invitation:
            invitation.rsvp = rsvp
            invitation.save()
        





class InvitaionViewSet(ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

    def perform_create(self, serializer):
        event = serializer.validated_data['event']
        event_info = EventInfo.objects.filter(event=event).first()
        if event_info:
            event_info.total_invitations += 1
            event_info.save()


        serializer.save(host=self.request.user)




class EventInfoViewSet(GenericViewSet):
    queryset = EventInfo.objects.all()
    serializer_class = EventInfoSerializer
    lookup_field = 'pk'

    def list(self,requset):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self,request, pk=None):
        event = self.get_object()
        if event:
            serializer = self.serializer_class(event)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)