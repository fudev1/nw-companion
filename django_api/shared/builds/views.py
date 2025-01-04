from django.shortcuts import render
from rest_framework import viewsets
from .models import NwBuild
from .serializers import NwBuildSerializer
from django.db.models import Q



# Create your views here.
class NwBuildViewSet(viewsets.ModelViewSet):
    queryset = NwBuild.objects.all()
    serializer_class = NwBuildSerializer

    def get_queryset(self):
        # Si l'utilisateur n'est pas authentifié, ne montrer que les builds publics
        if not self.request.user.is_authenticated:
            return NwBuild.objects.filter(is_public=True)
        
        # Sinon montrer les builds publics et ceux de l'utilisateur
        return NwBuild.objects.filter(
            Q(is_public=True) | 
            Q(creator=self.request.user)
        )