from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import NwRegion, NwServer
from .serializers import NwRegionSerializer, NwServerSerializer


class NwRegionViewSet(viewsets.ModelViewSet):
    """
    Liste des régions dispo pour New World
    Get /api/new-world/regions/
    """
    queryset = NwRegion.objects.filter(is_active=True)
    serializer_class = NwRegionSerializer
    permission_classes = [permissions.AllowAny]


class NwServerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Liste des serveurs, avec possibilité de filtrer par région
    GET /api/new-world/servers/
    GET /api/new-world/servers/?region=1
    """
    serializer_class = NwServerSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = NwServer.objects.filter(is_active=True)
        region_id = self.request.query_params.get('region', None)
        if region_id is not None:
            queryset = queryset.filter(region_id=region_id)
        return queryset.select_related('region')
    