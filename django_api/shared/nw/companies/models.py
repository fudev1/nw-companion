from django.db import models
from shared.tenants.models import Tenant


# Create your models here.
class NwCompany(Tenant):
    server = models.CharField(null=True, blank=True)
    faction = models.CharField(null=True, blank=True)

    # class Meta: 
    #     db_table = 'public_new_world_characters'

    def __str__(self):
        return f'{self.name} ({self.server} - {self.faction})'


