from rest_framework import viewsets
from .serializers import TenantSerializer, DomainSerializer
from .models import Tenant, Domain

# from tenant_users.tenants.tasks import provision_tenant
# from django_tenants.utils import get_tenant_model
# from rest_framework.response import Response
# from django.utils.text import slugify

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer