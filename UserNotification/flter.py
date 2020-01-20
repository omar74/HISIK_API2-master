import django_filters
from .models import NotificationUser
class UserNotificationFilter(django_filters.FilterSet):
    class Meta:
        model = NotificationUser
        fields = {
             'owner__id':['exact',],
             'Status':['exact',],
        }
 
