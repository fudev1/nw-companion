from rest_framework import viewsets
from .models import MemberProfile
from .serializers import MemberProfileSerializer


class MemberProfileViewSet(viewsets.ModelViewSet):
    queryset = MemberProfile.objects.all()
    serializer_class = MemberProfileSerializer

    def perform_create(self, serializer):
        #todo: ajouter une logique avant de sauvegarder
        #vérifier si un membre existe déjà
        serializer.save()
