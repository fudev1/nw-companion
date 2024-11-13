from rest_framework import viewsets, status
from .serializers import TenantSerializer, DomainSerializer
from rest_framework.response import Response
from .models import Tenant, Domain
from shared.new_world.models import NwCompany
from django.db import transaction

from datetime import date


from tenant_users.tenants.tasks import provision_tenant
from django.utils.text import slugify
from django.contrib.auth import get_user_model
# from django_tenants.utils import get_tenant_model
from rest_framework.views import APIView
from shared.tenants.tasks import provision_nwcompany
from rest_framework.decorators import action


User = get_user_model()

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer



    # @action(detail=False, methods=['post'], url_path='provision', url_name='provision')
    # def provision(self, request, *args, **kwargs):
    #     """
    #     Action personnalisée pour créer un Tenant avec NwCompany.
    #     """
    #     tenant_name = request.data.get('tenant_name')
    #     tenant_slug = request.data.get('tenant_slug')
    #     owner_email = request.data.get('owner_email')
    #     server = request.data.get('server')
    #     faction = request.data.get('faction')

    #     # Vérifier que tous les champs sont présents
    #     if not (tenant_name and tenant_slug and owner_email and server and faction):
    #         return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    #     # Récupérer l'utilisateur
    #     try:
    #         owner = User.objects.get(email=owner_email)
    #     except User.DoesNotExist:
    #         return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    #     # Appeler la fonction provision_nwcompany
    #     try:
    #         tenant, domain, nw_company = provision_nwcompany(
    #             tenant_name=tenant_name,
    #             tenant_slug=tenant_slug,
    #             user=owner,
    #             server=server,
    #             faction=faction,
    #             game_type="new_world"
    #         )
    #     except Exception as e:
    #         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #     return Response({'message': 'Tenant and NwCompany created successfully', 'tenant': tenant.schema_name}, status=status.HTTP_201_CREATED)


    # def perform_destroy(self, instance:Tenant):
    #     instance.delete_tenant()
    #     return instance
    # def perform_create(self, serializer:TenantSerializer):
    #     tenant = serializer._validated_data
    #     provision_tenant(tenant["name"], slugify(tenant["name"]+date.today()), tenant["owner"].email)

    #     return tenant
    
    # @transaction.atomic
    # def perform_update(self, serializer: TenantSerializer):
    #     tenant:Tenant= self.get_object()
        
    #     new_user = serializer.validated_data.get("owner")
        
    #     if new_user:
    #         tenant.transfer_ownership(new_user)

    #     return super().perform_update(serializer)

   

    # def perform_create(self, serializer):
    #     tenant_data = serializer.validated_data
    #     created_date = datetime.now()

    #     # Récupérer les informations nécessaires
    #     owner_email = tenant_data['owner'].email
    #     tenant_name = tenant_data['name']
    #     tenant_slug = slugify(tenant_name)
    #     game_type = tenant_data['game_type']

    #     try:
    #         user = User.objects.get(email=owner_email)
    #     except User.DoesNotExist:
    #         return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    #     # Provisionner le tenant de base
    #     with transaction.atomic():
    #         tenant_extra_data = {'game_type': game_type}

    #         tenant, domain = provision_tenant(
    #             tenant_name=tenant_name,
    #             tenant_slug=tenant_slug,
    #             owner=user,
    #             tenant_type=game_type,
    #             is_superuser=True,  # Ajuster en fonction des besoins
    #             tenant_extra_data=tenant_extra_data,
    #         )

    #         # Création de la compagnie NwCompany si le type est `new_world`
    #         if game_type == 'new_world':
    #             NwCompany.objects.create(
    #                 tenant_ptr_id=tenant.id,
    #                 name=tenant_data["name"],
    #                 game_type=tenant_data["game_type"],
    #                 owner=tenant_data["owner"],
    #                 paid_until=tenant_data.get("paid_until"),
    #                 basic_plan=tenant_data.get("basic_plan", True),
    #                 created=created_date  # Assurez-vous que ce champ est bien alimenté
    #             )

    #         return Response(TenantSerializer(tenant).data, status=status.HTTP_201_CREATED)


# class ProvisionCompany(APIView):
#     def post(self, request, *args, **kwargs):
#         tenant_name = request.data('tenant_name')
#         tenant_slug = request.data('tenant_slug')
#         owner_email = request.data('owner_email')
#         server = request.data.get('server')
#         faction = request.data.get('faction')

#         if not (tenant_name and tenant_slug and owner_email and server and faction):
#                 return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
            
#         # Récupérer l'utilisateur à partir de l'email fourni
#         User = get_user_model()
        
#         try:
#             owner = User.objects.get(email=owner_email)
#         except User.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#         # Appeler la fonction provision_nwcompany
#         try:
#             tenant, domain, nw_company = provision_nwcompany(
#                 tenant_name=tenant_name,
#                 tenant_slug=tenant_slug,
#                 user=owner,
#                 server=server,
#                 faction=faction,
#                 game_type="new_world"
#             )
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         return Response({'message': 'Tenant and NwCompany created successfully', 'tenant': tenant.schema_name}, status=status.HTTP_201_CREATED)




class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer