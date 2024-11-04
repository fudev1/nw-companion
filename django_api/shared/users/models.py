from django.db import models
from tenant_users.tenants.models import UserProfile

# Create your models here.
class TenantUser(UserProfile):
    name = models.CharField(max_length=100)
