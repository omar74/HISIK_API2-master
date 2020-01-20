from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .filter import ReviewFilter
from .models import Review
from .serializers import ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               = Review.objects.all()
    serializer_class       = ReviewSerializer
    filterset_class        = ReviewFilter
    search_field           = ('user__UserName','user__id','review__id','review__product','product__id')



class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               =  Review.objects.all()
    serializer_class       =  ReviewSerializer
    lookup_field= 'id'
    

