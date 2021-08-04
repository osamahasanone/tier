from django.urls import path
from .views import *

urlpatterns = [
    path('', URLList.as_view(), name='urls_list'),
    path('<int:pk>', URLDetail.as_view(),
         name='url_retrieve'),
    path('shorten', URLShortener.as_view(),
         name='url_shorten'),
]
