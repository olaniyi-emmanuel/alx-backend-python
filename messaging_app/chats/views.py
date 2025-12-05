from rest_framework import viewsets
from .models import Message, Conversation
from .serializers import ConversationSerializer, MessageSerializer
# Create your views here.

class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer

class MessageViewSet(viewsets.ViewSet):
    serializer_class = MessageSerializer

