from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


# Create your models here.

class Tenancy(TenantMixin):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey()
    created_on = models.DateField(auto_now_add=True)
    paid_until = models.DateField()
    basic_plan = models.BooleanField()



class Domain(DomainMixin):
    pass



