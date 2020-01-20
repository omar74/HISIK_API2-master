import django_filters
from .models import Like
class LikeFilter(django_filters.FilterSet):
    class Meta:
        model = Like
        fields = {
             'review__id':['exact',]
           , 'user__id':['exact',]
        }
 
