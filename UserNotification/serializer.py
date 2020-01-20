from .models import NotificationUser
from rest_framework import serializers
from product.serializer import ProductSerializer
from user.serializer import UserSerializer
from review.serializers import ReviewSerializer
class UserNotificationSerializer(serializers.ModelSerializer):
    NotifyuserDetalis  = serializers.SerializerMethodField(read_only=True)
    productDetails  = serializers.SerializerMethodField(read_only=True)
    reviewDetails  = serializers.SerializerMethodField(read_only=True)
    class Meta:
         model  = NotificationUser
         fields = ['id',
                 'Status',
                 'Type',
                 'owner',
                 'notifyuser',
                 'NotifyuserDetalis',
                 'productDetails',
                 'reviewDetails',
                 'product',
                 'review',
                 'updated',
                 'timestamp']
                 
    def get_NotifyuserDetalis(self,obj):
         return UserSerializer(obj.notifyuser).data
    def get_productDetails(self,obj):
         return ProductSerializer(obj.product).data
    def get_reviewDetails(self,obj):
         return ReviewSerializer(obj.review).data
   
   
 