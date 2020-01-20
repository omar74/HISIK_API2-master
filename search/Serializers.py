from rest_framework import serializers 
from .models import Search
from product.serializer import ProductSerializer

class SearchSerializers(serializers.ModelSerializer):
    PopProduct=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model  = Search
        fields = [
            'id',
            'text',
            'user',
            'product',
            'PopProduct',
            'updated',
            'timestamp'
        ]
    def get_PopProduct(self,obj):
         return ProductSerializer(obj.product).data