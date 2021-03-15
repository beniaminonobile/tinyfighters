from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response

from .models import OpenSeaItem
from .serializers import OpenSeaItemListSerializer, OpenSeaItemDetailSerializer


# Create your views here.
class OpenSeaItemListApiView(ListAPIView):
	permission_classes = (AllowAny,)
	queryset = OpenSeaItem.objects.all()
	serializer_class = OpenSeaItemListSerializer


class OpenSeaItemNewListApiView(OpenSeaItemListApiView):
	queryset = OpenSeaItem.objects.filter(status=1)
	permission_classes = (AllowAny, )

	def get(self, request, *args, **kwargs):
		list_response = super().get(request, *args, **kwargs)
		queryset = self.get_queryset()
		queryset.update(status=0)
		return list_response


class OpenSeaItemRetrieveApiView(RetrieveAPIView):
	permission_classes = (AllowAny,)
	queryset = OpenSeaItem.objects.all()
	serializer_class = OpenSeaItemDetailSerializer

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		return Response(instance.meta)

