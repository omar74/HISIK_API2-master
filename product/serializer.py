from rest_framework import serializers
from .models import Product
from brand.models import Brand
from category.models import Category
from brand.serializer import BrandSerializer
from category.serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    product_Brand=serializers.SerializerMethodField(read_only=True)
    product_Category=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model  = Product
        fields = [
             'id' 
             ,'name'
             ,'Description'
             ,'brand'
             ,'product_Brand'
             ,'Category'
             ,'product_Category'
             ,'ImageURL'
        ]
    def get_product_Brand(self,obj):
         return BrandSerializer(obj.brand).data
    def get_product_Category(self,obj):
         return CategorySerializer(obj.Category).data 
