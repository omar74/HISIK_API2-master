import django_filters
from .models import Favourite
class favouriteFilter(django_filters.FilterSet):
    class Meta:
        model = Favourite
        fields = {
             'user__id':['exact',]
           , 'product__id':['exact',]
        }
 
