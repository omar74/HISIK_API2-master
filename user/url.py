from .views import UserDetailView,UserListView#,UserFormView
from django.urls import path

urlpatterns = [
    path('', UserListView.as_view(),name='productListCreate'),

    #path('register', UserFormView.as_view(),name='register'),

    path('<int:id>/', UserDetailView.as_view(),name='productDetail'),
] 