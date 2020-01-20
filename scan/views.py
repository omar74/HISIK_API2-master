from django.shortcuts import render
from .serializer import ScanSerializer
from .models import Scan
from rest_framework import generics

# Create your views here.
class ScanListView(generics.ListCreateAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               = Scan.objects.all()
    serializer_class       =  ScanSerializer
    search_fields          = ('user__UserName','user__id','user__Email')

class ScanDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Scan.objects.all()
    serializer_class       =  ScanSerializer
    lookup_field = 'id'
    