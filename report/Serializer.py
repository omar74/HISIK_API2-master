from rest_framework import serializers 
from report.models import Report 
from user.serializer import UserSerializer
from product.serializer import ProductSerializer

class ReportSerializers(serializers.ModelSerializer):
    PopUser=serializers.SerializerMethodField(read_only=True)
    PopProduct=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model  = Report
        fields = [
            'id',
            'product',
            'user',
            'Description',
            'name',
            'brand',
            'category',
            'comment',
            'PopUser',
            'PopProduct',
            'updated',
            'timestamp'
        ]

    def get_PopUser(self,obj):
         return UserSerializer(obj.user).data

    def get_PopProduct(self,obj):
          return ProductSerializer(obj.product).data

