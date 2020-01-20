from django.shortcuts import render
from .models import Report 
from .Serializer import ReportSerializers
from rest_framework import generics

# Create your views here.

class ReportListView(generics.ListCreateAPIView):
    permission_classes       = []
    authentication_classes   = []
    queryset                 = Report.object.all()
    serializer_class         = ReportSerializers

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes       = []
    authentication_classes   = []
    queryset                 = Report.object.all()
    serializer_class         = ReportSerializers
    lookup_field             = 'id'

