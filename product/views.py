from django.shortcuts import render
from .models import Product
from .serializer import ProductSerializer
from .filter import ProductFilter
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

import json 
import requests
# Create your views here. 
class ProductListView(generics.ListCreateAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Product.objects.all()
    serializer_class       =  ProductSerializer
    filterset_class        =  ProductFilter
    search_fields          = ('id','Category__Name','brand__Name','name',)

    # def get_queryset(self):
    #     category = self.request.GET.get('Cname')
    #     qs = Product.objects.filter(Category__Name=category)
    #     return qs
     


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Product.objects.all()
    serializer_class       =  ProductSerializer
    lookup_field = 'id'

@api_view(['GET'])
def GetLinks(request,product):
    result=requests.get("https://api.serpwow.com/live/search?api_key=D0291E8A&q="+product+"&gl=eg&hl=en&search_type=shopping")
    return Response(result.json())


    