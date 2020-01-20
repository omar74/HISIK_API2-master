from django.shortcuts import render
from .models import Favourite
from .serializer import FavouriteSerializer
from .filter import favouriteFilter
from rest_framework import generics

# Create your views here.
class FavouriteListView(generics.ListCreateAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Favourite.objects.all()
    serializer_class       =  FavouriteSerializer
    filterset_class        =  favouriteFilter
    search_fields          = ('user__UserName','user__id','user__Email')

class FavouriteDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Favourite.objects.all()
    serializer_class       =  FavouriteSerializer
    lookup_field = 'id'
    