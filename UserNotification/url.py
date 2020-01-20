from django.urls import path
from .views import UserNotificationDetailedView, UserNotificationListView

urlpatterns = [
    path('', UserNotificationListView.as_view()),
    path('<int:id>/', UserNotificationDetailedView.as_view()),
]
