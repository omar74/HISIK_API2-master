from .views import ReportDetailView , ReportListView
from django.urls import path

urlpatterns = [
    path('', ReportListView.as_view(),name='ReportListCreate'),
    path('<int:id>/', ReportDetailView.as_view(),name='ReportDetail'),
]
