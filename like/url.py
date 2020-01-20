from .views import LikeList,LikeDetailView
from django.urls import path

urlpatterns = [
    path('', LikeList.as_view(),name='LikeListCreate'), #/replay -- /create
    path('<int:id>/', LikeDetailView.as_view(),name='LikeDetail'), #/replay/id -- Retrieve/update/delete
]
