from django.db import models

# Create your models here.

class Event(models.Model):
    organizer = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE)
    eventName = models.TextField()
    eventDate = models.DateField()
    hours = models.TimeField()
    location = models.TextField()
    description = models.TextField()
    guestsAmount = models.IntegerField()
    


class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user =  models.ForeignKey(to='users.CustomUser', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=True)


class Invitation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    host = models.ForeignKey(to='users.CustomUser', on_delete=models.CASCADE, related_name='host')
    guest = models.ForeignKey(to='users.CustomUser', on_delete=models.CASCADE, related_name='guest')
    rsvp = models.ForeignKey(RSVP, on_delete=models.CASCADE, null=True, blank=True)




class EventInfo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    host = models.ForeignKey(to='users.CustomUser', on_delete=models.CASCADE)
    total_invitations = models.IntegerField(default=0)
    total_rsvps = models.IntegerField(default=0)
    total_accepted_rsvps = models.IntegerField(default=0)
    total_rejected_rsvps = models.IntegerField(default=0)
    invitaion_accepted_rsvps = models.IntegerField(default=0)
    invitation_rejected_rsvps = models.IntegerField(default=0)



class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    text = models.TextField(blank=True,null=True)


class FileUpload(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_files')
    file = models.FileField(blank=True, null=True)
