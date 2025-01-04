from rest_framework import serializers
from .models import NwRegion, NwServer


class NwRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NwRegion
        fields = ['id', 'name']

class NwServerSerializer(serializers.ModelSerializer):
    region_name = serializers.CharField(source='region.name', read_only=True)

    class Meta:
        model = NwServer
        fields = ['id', 'name', 'region', 'region_name']