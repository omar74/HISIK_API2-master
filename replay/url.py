from .views import ReplayList,ReplayDetailView
from django.urls import path

urlpatterns = [
    path('', ReplayList.as_view(),name='ReplayListCreate'), #/replay -- /create
    path('<int:id>/', ReplayDetailView.as_view(),name='ReplayDetail'), #/replay/id -- Retrieve/update/delete
]
