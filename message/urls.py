from .views import MessageListView , MessageDetailView
from django.urls import path

urlpatterns = [
    path('', MessageListView.as_view(),name='MessageListCreate'),
    path('<int:id>/', MessageDetailView.as_view(),name='MessageDetail'),
]