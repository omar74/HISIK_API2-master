from django.shortcuts import render
from .models import Message 
from .Serializer import MessageSerializers
from rest_framework import generics

class MessageListView(generics.ListCreateAPIView):
    permission_classes       = []
    authentication_classes   = []
    queryset                 = Message.object.all()
    serializer_class         = MessageSerializers

class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes       = []
    authentication_classes   = []
    queryset                 = Message.object.all()
    serializer_class         = MessageSerializers
    lookup_field             = 'id'
