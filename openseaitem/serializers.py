from rest_framework import serializers
from .models import OpenSeaItem


class OpenSeaItemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpenSeaItem
        fields = '__all__'
