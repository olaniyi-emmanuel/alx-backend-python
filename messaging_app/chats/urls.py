from django.db import router
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import ConversationViewSet, MessageViewSet

routers = routers.DefaultRouter()
routers.register(r'conversations', ConversationViewSet, basename='conversations')
routers.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = [path('conversations', include(routers.urls)),
               path('messages', include(routers.urls)),]
