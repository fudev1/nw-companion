from rest_framework import viewsets
from .models import DiscordRole
from .serializers import DiscordRoleSerializer


class DiscordRoleViewSet(viewsets.ModelViewSet):
    queryset = DiscordRole.objects.all()
    serializer_class = DiscordRoleSerializer