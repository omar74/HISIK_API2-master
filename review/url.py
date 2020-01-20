from .views import ReviewList,ReviewDetailView
from django.urls import path

urlpatterns = [
    path('', ReviewList.as_view(),name='ReviewListCreate'), #/review -- /create
    path('<int:id>/', ReviewDetailView.as_view(),name='ReviewDetail'), #/review/id -- Retrieve/update/delete
]
