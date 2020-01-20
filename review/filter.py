import django_filters
from .models import Review
class ReviewFilter(django_filters.FilterSet):
    class Meta:
        model = Review
        fields = {
             'product__id':['exact',]
             ,'user__id':['exact',]
        }
 
