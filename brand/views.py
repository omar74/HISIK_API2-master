from django.shortcuts import render
from .models import Brand
from .serializer import BrandSerializer
from rest_framework import generics

# Create your views here.
class BrandListView(generics.ListCreateAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Brand.objects.all()
    serializer_class       =  BrandSerializer
    search_fields          = ('Name',)
class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Brand.objects.all()
    serializer_class       =  BrandSerializer
    lookup_field = 'Name'
    