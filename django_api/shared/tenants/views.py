from rest_framework import viewsets
from .serializers import TenantSerializer, DomainSerializer
from .models import Tenant, Domain


from tenant_users.tenants.tasks import provision_tenant
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from rest_framework.decorators import action


User = get_user_model()

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer