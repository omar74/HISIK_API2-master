from rest_framework import serializers
from .models import Scan
from product.serializer import ProductSerializer


class ScanSerializer(serializers.ModelSerializer):
    productDetails=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model  = Scan
        fields = [
              'id'
             ,'user'
             ,'product'
             ,'productDetails'
             ,'brand'
             ,'Category'
             ,'Blocked'
             ,'satisfy'
             ,'ImageURL'
             ,'updated'
             ,'timestamp'
        ]
    def get_productDetails(self,obj):
         return ProductSerializer(obj.product).data
