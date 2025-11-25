#from django.utils import timezone
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class userProfile(models.Model): 
    role = [
        ('admin', 'Admin'),
        ('host', 'Host'),
        ('guest', 'Guest'),
    ]


class user(AbstractUser): 
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False),
    username = models.Charfield(max_lenth=120, unique=True, null=False, db_index = True)
    first_name = models.TextField(null=False),
    last_name = models.TextField(null= False)
    email = models.EmailField(unique=True, null=False, db_index = True)
    phone_number = models.TextField(null= False)
    role = models.CharField(max_length=10, choices=userProfile.role, default='guest')
    created_at = models.TimeField(auto_now_add=True)
    #password = models.CharField(null=False,  max_length=50)
    

class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, null=False, db_index = True )
    participants_id = models.ForeignKey("user", on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, null=False)
    sender_id = models.ForeignKey("user", on_delete=models.CASCADE)
    message_body = models.TextField(null=False)
    sent_at = models.TimeField(auto_now_add=True)
