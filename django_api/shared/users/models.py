from django.db import models
from tenant_users.tenants.models import UserProfile

# Create your models here.
class TenantUser(UserProfile):
    # discord_id = models.BigIntegerField(primary_key=True)
    # username = models.CharField(max_length=100, blank=True, null=True)
    # avatar = models.CharField(max_length=100, blank=True, null=True)
    # locale = models.CharField(max_length=100, blank=True, null=True)
    # last_login = models.DateTimeField()
    # email = models.EmailField(unique=True)


    last_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self): 
        return str(self.email)
   
