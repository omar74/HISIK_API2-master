from django.urls import path
from .views import AdminNotficationDetailedView,AdminNotificationListView

urlpatterns = [
    path('', AdminNotificationListView.as_view()),
    path('<str:type>/', AdminNotficationDetailedView.as_view()),
]