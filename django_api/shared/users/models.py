from django.db import models
from tenant_users.tenants.models import UserProfile

# Create your models here.
class TenantUser(UserProfile):
    last_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self): 
        return str(self.email)
   
