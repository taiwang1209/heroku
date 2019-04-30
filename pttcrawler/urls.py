"""pttcrawler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers
from rest_framework.authtoken import views

from index.views import get_index, show, gallery, delete, PttArticleViewSet, ImagesViewSet

from aprp.views import CategoryList, MarketList, ProductList, DailyTranList


router = routers.SimpleRouter()
router.register(r'all', PttArticleViewSet)
router.register(r'img', ImagesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', get_index),
    path('index/show/', show),
    path('index/gallery/', gallery),
    path('index/delete/', delete),
    url('api/', include(router.urls)),
    url(r'^api/category/$', CategoryList.as_view()),
    url(r'^api/market/$', MarketList.as_view()),
    url(r'^api/product/$', ProductList.as_view()),
    url(r'^api/dailytran/$', DailyTranList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
]
