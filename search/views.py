from django.shortcuts import render
from .models import Search 
from product.models import Product
from brand.models import Brand
from category.models import Category
from product.serializer import ProductSerializer
from .Serializers import SearchSerializers
from rest_framework import generics
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.decorators import api_view


class SearchListView(generics.ListCreateAPIView):
    permission_classes       = []
    authentication_classes   = []
    queryset                 = Search.object.all()
    serializer_class         = SearchSerializers

class SearchDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes       = []
    authentication_classes   = []
    queryset                 = Search.object.all()
    serializer_class         = SearchSerializers
    lookup_field             = 'id'

@api_view(['Get'])
def PopualerSearch(request):
    final=[]
    popularProduct=Search.object.exclude(product__id__isnull=True).values('product__id').annotate(ProCount=Count('product__id')).order_by('-ProCount')[:5]
    for pro in popularProduct:
        product=Product.objects.get(id=pro['product__id'])
        final.append(product)
    serialize=ProductSerializer(final,many=True).data
    return Response(serialize)

@api_view(['GET'])
def RecommandedSearch(request,userid):
    userSearch = Search.object.filter(user__id=userid).exclude(product__id__isnull=True).values('product__id')
    productsBrand  = Product.objects.filter(id__in=userSearch).values('brand__id')
    RecommedProducts = Product.objects.filter(brand__id__in=productsBrand)
    serialize = ProductSerializer(RecommedProducts,many=True).data
    return Response(serialize)
