# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'openseaitem'

urlpatterns = [
    # API URLS
    path('api/opensea-item/', views.OpenSeaItemListApiView.as_view(), name='open-sea-item'),
	path('api/opensea-item/new/', views.OpenSeaItemNewListApiView.as_view(), name='open-sea-item'),
]
