from rest_framework import viewsets, filters
from .models import Message, Conversation
from .serializers import ConversationSerializer, MessageSerializer
# Create your views here.

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter]

class MessageViewSet(viewsets.ViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter]


