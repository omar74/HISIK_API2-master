from rest_framework import serializers
from .models import Replay,Review
from review.serializers import ReviewSerializer
from user.serializer import UserSerializer
class ReplaySerializer(serializers.ModelSerializer):
    AllReviews=serializers.SerializerMethodField(read_only=True)
    owner=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model= Replay
        fields=('id','review','user','text','owner','AllReviews','timestamp','updated')
    
    def get_AllReviews(self,obj):
         return ReviewSerializer(obj.review).data
    def get_owner(self,obj):
         return UserSerializer(obj.user).data

           
    