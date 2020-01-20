"""HISIK_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/brand/',include('brand.url')),
    path('api/category/',include('category.url')),
    path('api/product/',include('product.url')),
    path('api/favourite/',include('favourite.url')),
    path('api/userNoitifaction/',include('UserNotification.url')),
    path('api/adminNoitifaction/',include('adminNotification.urls')),
    path('api/user/',include('user.url')),
    path('api/scan/',include('scan.url')),
    path('api/review/',include('review.url')),
    path('api/replay/',include('replay.url')),
    path('api/like/',include('like.url')),
    path('api/report/',include('report.urls')),
    path('api/message/',include('message.urls')),
    path('api/search/',include('search.urls'))

    
]
