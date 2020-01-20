from rest_framework import serializers
from .models import Favourite
from product.serializer import ProductSerializer 

class FavouriteSerializer(serializers.ModelSerializer):
    ProductDetails = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model  = Favourite
        fields = [
             'id'
             ,'user'
             ,'product'
             ,'ProductDetails'
             ,'timestamp'
        ]
    def get_ProductDetails(self,obj):
         return ProductSerializer(obj.product).data