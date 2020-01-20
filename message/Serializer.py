from rest_framework import serializers 
from .models import Message
from user.serializer import UserSerializer
from product.serializer import ProductSerializer

class MessageSerializers(serializers.ModelSerializer):
    PopUser=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model  = Message
        fields = [
            'id',
            'text',
            'user',
            'PopUser',
            'updated',
            'timestamp'
        ]

    def get_PopUser(self,obj):
         return UserSerializer(obj.user).data
