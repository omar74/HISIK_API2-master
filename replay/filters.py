import django_filters
from .models import Replay
class ReplayFilter(django_filters.FilterSet):
    class Meta:
        model = Replay
        fields = {
             'review__id':['exact',]
             ,'user__id':['exact',]
        }