from .views import SearchListView , SearchDetailView ,PopualerSearch , RecommandedSearch
from django.urls import path

urlpatterns = [
    path('', SearchListView.as_view(),name='SearchListCreate'),
    path('<int:id>/', SearchDetailView.as_view(),name='SearchDetail'),
    path('popular/',PopualerSearch),
    path('recommanded/<int:userid>/',RecommandedSearch),
]