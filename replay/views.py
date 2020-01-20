from django.shortcuts import render

from rest_framework import generics
from .filters import ReplayFilter


from .models import Replay
from .serializer import ReplaySerializer


class ReplayList(generics.ListCreateAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               = Replay.objects.all()
    serializer_class       = ReplaySerializer
    filterset_class        = ReplayFilter

    search_field           =('user__UserName','user__id','review__id','review__product','product__id')


class ReplayDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Replay.objects.all()
    serializer_class       =  ReplaySerializer
    lookup_field= 'id'
    

