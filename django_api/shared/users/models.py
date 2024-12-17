from django.db import models
from tenant_users.tenants.models import UserProfile
from django.utils.timezone import now

# Create your models here.
class TenantUser(UserProfile):
    discord_id = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    global_name = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    locale = models.CharField(max_length=10, blank=True, null=True)
    last_login = models.DateTimeField(null=True, blank=True, default=now)

    public_flags = models.IntegerField(null=True, blank=True)               # drapeau public (badge nitro)
    mfa_enabled = models.BooleanField(default=False)                        # auth 2 facteur
    banner = models.CharField(max_length=500, null=True, blank=True)        
    banner_color = models.CharField(max_length=7, null=True, blank=True)    
    accent_color = models.IntegerField(null=True, blank=True)               
    verified = models.BooleanField(default=False)

    def __str__(self): 
        return f"{self.global_name} ({self.email})"
   



class UserInfo(models.Model):
    user = models.OneToOneField(TenantUser, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Profil de {self.user.username}"                           