from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import NwCharacter
from .serializers import NwCharacterSerializer


"""
# PUBLIC :
GET     /api/characters/new-world/                  - Liste tous les personnages
GET     /api/characters/new-world/search/?q=query   - Recherche publique
GET     /api/characters/new-world/recent/           - Derniers personnages créés

# USER :
GET     /api/characters/new-world/my_characters/    - Ses personnages
POST    /api/characters/new-world/                  - Créer un personnage
PUT     /api/characters/new-world/{id}/             - Modifier son personnage
DELETE  /api/characters/new-world/{id}/             - Supprimer son personnage
"""


class NwCharacterViewSet(viewsets.ModelViewSet):
    queryset = NwCharacter.objects.all()
    serializer_class = NwCharacterSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'search']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    

    @action(detail=False, methods=['GET'])
    def my_characters(self, request):
        """Vue "mes personnages" quand l'user est connecté"""
        characters = NwCharacter.objects.filter(user=request.user)
        serializer = self.get_serializer(characters, many=True)
        return Response(serializer.data)
    

    @action(detail=False, methods=['GET'])
    def search(self, request):
        """Recherche publique de personnages"""
        query = request.query_params.get('q', '')
        characters = NwCharacter.objects.filter(
            Q(name__icontains=query) |
            Q(server__icontains=query) |
            Q(faction__icontains=query)
        )
        serializer = self.get_serializer(characters, many=True)
        return Response(serializer.data)
    

    @action(detail=False, methods=['GET'])
    def recent(self, request):
        """Liste des perso récemment créés"""
        characters = NwCharacter.objects.order_by('-created_at')[:10]
        serializer = self.get_serializer(characters, many=True)
        return Response(serializer.data)

