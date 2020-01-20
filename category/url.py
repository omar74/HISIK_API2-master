from .views import CategoryDetailView,CategoryListView
from django.urls import path

urlpatterns = [
    path('', CategoryListView.as_view(),name='CategoryListCreate'),
    path('<str:Name>/', CategoryDetailView.as_view(),name='CategoryDetail'),
]
