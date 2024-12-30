from rest_framework import viewsets
from .serializers import NwCompanySerializer
from .models import NwCompany
from django.utils.text import slugify
from shared.tenants.tasks.provision_tenant import provision_tenant



class NwCompanyViewSet(viewsets.ModelViewSet):
    queryset = NwCompany.objects.all()
    serializer_class = NwCompanySerializer

    def perform_create(self, serializer: NwCompanySerializer):
        # Récupérer les données validées
        tenant_data = serializer.validated_data

        tenant_name = tenant_data['name']
        tenant_slug = slugify(tenant_name)

        # Définir l'owner à partir de l'utilisateur connecté
        # owner = self.request.user

        # Extraire les données spécifiques pour extra_data
        tenant_extra_data = {
            "server": tenant_data["server"],
            "faction": tenant_data["faction"]
        }

        # créer le tenant et le domaine associés => provision_tenant
        try:
            tenant, domain = provision_tenant(
                tenant_name=tenant_data["name"],
                tenant_slug=tenant_slug,
                owner=tenant_data["owner"],
                # tenant_type=tenant_data.get("game_type", "new_world"),
                tenant_type="new_world",     # je défini directement à new world
                tenant_extra_data=tenant_extra_data,
            )
        except Exception as e:
            # Si quelque chose ne va pas, lever l'exception pour que Django puisse la traiter
            print(f"Erreur lors du provisionnement du tenant : {str(e)}")
            raise e

        # Relier le tenant créé au serializer
        serializer.instance = tenant

        return serializer
    


        

