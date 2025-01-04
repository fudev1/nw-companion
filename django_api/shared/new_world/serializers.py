from rest_framework import serializers
from .models import NwRegion, NwServer, NwRole, NwFaction


class NwRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NwRegion
        fields = ['id', 'name']

class NwServerSerializer(serializers.ModelSerializer):
    region_name = serializers.CharField(source='region.name', read_only=True)

    class Meta:
        model = NwServer
        fields = ['id', 'name', 'region', 'region_name']


class NwRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NwRole
        fields = ['id', 'name', 'description', 'icon_url' ]


class NwFactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NwFaction
        fields = ['id', 'name']