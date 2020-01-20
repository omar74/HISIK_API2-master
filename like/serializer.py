from rest_framework import serializers
from .models import Review,Like
from review.serializers import ReviewSerializer

class LikeSerializer(serializers.ModelSerializer):
    AllReviews=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model= Like
        fields=('id','review','user','AllReviews')
    
    def get_AllReviews(self,obj):
         return ReviewSerializer(obj.review).data

           
    