from rest_framework import serializers
from .models import Review
from product.serializer import ProductSerializer
from user.serializer import UserSerializer
class ReviewSerializer(serializers.ModelSerializer):
    productDetails=serializers.SerializerMethodField(read_only=True)
    userData=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model= Review
        fields=('id','user','text','rate','product','productDetails','userData','timestamp','updated')
    
    
    def get_productDetails(self,obj):
         return ProductSerializer(obj.product).data
    def get_userData(self,obj):
         return UserSerializer(obj.user).data
    
    


           
    