from rest_framework import serializers 
from .models import NotificationAdmin
from review.serializers import ReviewSerializer
from scan.serializer import ScanSerializer
class NotificationAdminSerializer(serializers.ModelSerializer):
    ReviewData =serializers.SerializerMethodField(read_only=True)
    scanData =serializers.SerializerMethodField(read_only=True)

    class Meta:
        model  = NotificationAdmin
        fields = ['Status','Type','ProductReviewID','ReviewData','ScanId','scanData','updated','timestamp']
    
    def get_ReviewData(self,obj):
         return ReviewSerializer(obj.ProductReviewID).data
    def get_scanData(self,obj):
         return ScanSerializer(obj.ScanId).data
    