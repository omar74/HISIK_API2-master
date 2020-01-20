from .views import FavouriteDetailView,FavouriteListView
from django.urls import path

urlpatterns = [
    path('', FavouriteListView.as_view(),name='FavouriteListCreate'),
    path('<int:id>/', FavouriteDetailView.as_view(),name='FavouriteDetail'),
]
