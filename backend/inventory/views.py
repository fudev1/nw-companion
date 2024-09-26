from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import ItemSerializer
from .models import Item


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
