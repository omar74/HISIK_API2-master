from .views import ScanDetailView,ScanListView
from django.urls import path

urlpatterns = [
    path('', ScanListView.as_view(),name='ScanListCreate'),
    path('<int:id>/', ScanDetailView.as_view(),name='ScanDetail'),
]
