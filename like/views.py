from django.shortcuts import render
from .filter import LikeFilter
from rest_framework import generics

from .models import Like
from .serializer import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               = Like.objects.all()
    serializer_class       = LikeSerializer
    filterset_class        = LikeFilter
    search_field           = ('id')



class LikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Like.objects.all()
    serializer_class       =  LikeSerializer
    lookup_field= 'id'
    

