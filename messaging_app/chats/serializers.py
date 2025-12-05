from rest_framework import serializers
from .models import User, Conversation, Message

class UsersSerializer(serializers.ModelSerializer): 
    full_name  = serializers.SerializerMethodField()
    class Meta: 
        model = User
        fields = [
            'user_id',
            'username', 
            'full_name', 
            'first_name', 
            'last_name', 
            'email'
            ]
    def get_sender_username(self, obj): 
        return obj.sender.username
    
    def check_username(self, value): 
        if user.objects.filter(username=value).is_exists():
            raise serializers.ValidationError("Username already exists")



class MessageSerializer(serializers.ModelSerializer): 
    text = serializers.CharField(max_length=500)
    sender = UsersSerializer(read_only=True)
    class Meta: 
        model = Message 
        fields = [
            'message_id',
            'sender', 
            'sender_id',
            'message_body', 
            'sent_at'
        ]

class ConversationSerializer(serializers.ModelSerializer): 
    messsage = MessageSerializer(read_only=True, many=True)
    class Meta: 
        model = Conversation
        fields = [
            'conversation_id', 
            'participants_id',
            'created_at'
        ]