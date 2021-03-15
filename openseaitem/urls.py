# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'openseaitem'

urlpatterns = [
    # API URLS
    path('api/openseaitem/', views.OpenSeaItemListApiView.as_view(), name='openseaitem-list'),
	path('api/openseaitem/<int:pk>/', views.OpenSeaItemRetrieveApiView.as_view(), name='openseaitem-retrieve'),
	path('api/openseaitem/new/', views.OpenSeaItemNewListApiView.as_view(), name='openseaitem-list-new'),
]
