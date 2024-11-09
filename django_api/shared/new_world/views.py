from rest_framework import viewsets
from .serializers import NwCompanySerializer
from .models import NwCompany

# from tenant_users.tenants.tasks import provision_tenant
# from django_tenants.utils import get_tenant_model
# from rest_framework.response import Response
# from django.utils.text import slugify

# Create your views here.
class NwCompanyViewSet(viewsets.ModelViewSet):
    queryset = NwCompany.objects.all()
    serializer_class = NwCompanySerializer












    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     company = get_tenant_model().objects.get(id=response.data['id'])

    #     domain_name = f"{company.schema_name}.localhost"
    #     Domain.objects.create(
    #         domain=domain_name,
    #         tenant=company,
    #         is_primary=True
    #     )

    #     return response


    # def create(self, request, *args, **kwargs):
    #     # Assurer que les données du sérialiseur sont valides
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     # Extraire les données nécessaires pour créer le tenant
    #     validated_data = serializer.validated_data
    #     owner = request.user
    #     schema_name = validated_data['schema_name']
    #     tenant_name = validated_data['name']
    #     tenant_slug = slugify(tenant_name)  # Convertir le nom en un slug utilisable

    #     # Appeler provision_tenant pour créer la compagnie et le domaine associé
    #     tenant, domain = provision_tenant(
    #         owner=owner,                   # Utilisateur propriétaire
    #         schema_name=schema_name,       # Nom du schéma
    #         tenant_name=tenant_name,       # Nom de la compagnie
    #         tenant_slug=tenant_slug        # Slug de la compagnie
    #     )

    #     # Créer une réponse pour indiquer la création réussie
    #     response_data = {
    #         'id': tenant.id,
    #         'schema_name': tenant.schema_name,
    #         'owner': tenant.owner.id,
    #         'domain_set': list(tenant.domain_set.values_list('domain', flat=True))
    #     }
        
    #     return Response(response_data)
