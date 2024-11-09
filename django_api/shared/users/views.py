from rest_framework import viewsets
from .serializers import TenantUserSerializer
from .models import TenantUser


# Create your views here.
class TenantUserViewSet(viewsets.ModelViewSet):
    queryset = TenantUser.objects.all()
    serializer_class = TenantUserSerializer


    # #todo: créer une fonction pour la création d'un utilisateur qui comprend les méthode suivantes : 
    # def perform_create(self, serializer):
    #     user: TenantUser = serializer.save()

    #     pass

    #     #todo: Générer un code à 4 chiffres

    #     #todo: Mettre en cache le code pendant 2 minutes

    #     #todo: Envoyer un email avec le code de vérification

