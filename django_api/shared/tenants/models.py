from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from tenant_users.tenants.models import TenantBase
from shared.users.models import TenantUser
from django_tenants.utils import get_tenant_type_choices

# Create your models here.

class Tenant(TenantBase):
    game_type = models.CharField(max_length=100, choices=get_tenant_type_choices())
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(TenantUser, on_delete=models.CASCADE, related_name="owned_tenants")

    paid_until = models.DateField(null=True, blank=True)
    basic_plan = models.BooleanField(default=True)

    auto_create_group_on_schema_create = True
    auto_create_group_on_user_create = True
    auto_create_permissions_on_schema_create = True
    auto_create_permissions_on_user_create = True
    auto_create_schema = True
    auto_drop_schema = True

    def __str__(self):
        return self.schema_name
    

class Domain(DomainMixin):
    pass
