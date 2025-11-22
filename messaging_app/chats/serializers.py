from rest_framework import serializer 
from .models import user, Conversation, Message 

User = get_user_model()
sender_username = serializer.SerializerMethodField()

class Users(serializers.ModelSerializer): 
    class Meta: 
        model = user
        fields = [
            'user_id', 
            'first_name', 
            'last_name', 
            'email'
            ]
    def get_sender_username(self, obj): 
        return obj.sender.username
    

class conversation(serializers.ModelSerializer): 
    class Meta: 
        model = Conversation
        fields = [
            'conversation_id', 
            'participants_id',
            'created_at'
        ]

class message(serializers.ModelSerializer): 
    class Meta: 
        model = Message 
        fields = [
            'message_id',
            'sender_id',
            'message_body', 
            'sent_at'
        ]
