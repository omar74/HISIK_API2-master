import django_filters
from .models import Product
class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
             'brand__Name':['icontains',]
           , 'Category__Name':['icontains',]
           , 'name':['icontains',]
        }
 
