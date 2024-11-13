from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Character
from .serializers import CharacterSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    """
    CRUD operation pour Character Model
    """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    # permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def detailed_view(self, request, pk=None):
        """
        custom action pour get le détail des info Character
        """
        character = self.get_object()
        serializer = self.get_serializer(character)
        return Response(serializer.data)


class CharacterListView(APIView):
    """
    APIView pour lister tous les Characters
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        character = Character.objects.all()
        serializer = CharacterSerializer(character, many=True)
        return Response(serializer.data)


class CharacterDetailView(APIView):
    """
    APIView pour retrive un character detail. Utile pour formater une reponse custom
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            character = Character.objects.all(pk=pk)
        except Character.DoesNotExist:
            return Response({'error': 'Character not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        try:
            character = Character.objects.get(pk=pk)
        except Character.DoesNotExist:
            return Response({'error': 'Character not found'}, status=status.HTTP_404_NOT_FOUND)

        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, *args, **kwargs):
        try:
            character = Character.objects.get(pk=pk)
        except Character.DoesNotExist:
            return Response({'error': 'Character not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CharacterSerializer(character, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
