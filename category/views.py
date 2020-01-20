from django.shortcuts import render
from .models import Category
from .serializer import CategorySerializer
from rest_framework import generics

# Create your views here.
class CategoryListView(generics.ListCreateAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Category.objects.all()
    serializer_class       =  CategorySerializer
    search_fields          = ('Name',)

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Category.objects.all()
    serializer_class       =  CategorySerializer
    lookup_field = 'Name'
    