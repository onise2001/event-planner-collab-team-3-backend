from rest_framework import serializers
from .models import Event, RSVP, Invitation, EventInfo, Comment
from users.serializers import CustomUserSerializer
from users.models import CustomUser



class EventSerializer(serializers.ModelSerializer):
    organizer = CustomUserSerializer(read_only=True)
    class Meta:
        model = Event
        fields = '__all__'

    
    
    def create(self,validated_data):
            new_event = Event.objects.create(**validated_data)
            if new_event:
                event_info = EventInfo.objects.create(event=new_event,host=new_event.organizer)
                event_info.save()
            new_event.save()
            return new_event

    


class RSVPSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), write_only=True, source="event")
    user = CustomUserSerializer(read_only=True)
    #user_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), write_only=True, source='user')
    class Meta:
        model = RSVP
        fields = '__all__'



class InvitationSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    event_id = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), write_only=True, source="event")
    host = CustomUserSerializer(read_only=True)
    #host_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), write_only=True, source='host')
    guest = CustomUserSerializer(read_only=True)
    guest_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), write_only=True, source='guest')
    rsvp = RSVPSerializer(read_only=True)
    
    class Meta:
        model = Invitation
        fields = '__all__'




class EventInfoSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    host  = CustomUserSerializer(read_only=True)
    class Meta:
        model = EventInfo
        fields = '__all__'
        


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'