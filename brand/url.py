from .views import BrandDetailView,BrandListView
from django.urls import path

urlpatterns = [
    path('', BrandListView.as_view(),name='BrandListCreate'),
    path('<str:Name>/', BrandDetailView.as_view(),name='BrandDetial'),
]
