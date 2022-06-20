from django.db import models
from authentication.models import Profile
from django.utils.timezone import now

# Create your models here.
class Group(models.Model):
    admin = models.ForeignKey(
        Profile, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    ) # Personal groups has no admin
    name = models.CharField(
        max_length=64,
        blank=True,
        null=True
    )
    picture = models.ImageField(
        upload_to='group/',
        blank=True,
        null=True
    )
    members = models.ManyToManyField(
        Profile, 
        related_name='members'
    )
    is_personal = models.BooleanField(
        default=True
    )
    

class Message(models.Model):
    sender = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )
    sent_time = models.DateTimeField(
        default=now
    )
    
    
class TextMessage(models.Model):
    text = models.TextField()
    message = models.ForeignKey(
        Message, 
        on_delete=models.CASCADE
    )
    