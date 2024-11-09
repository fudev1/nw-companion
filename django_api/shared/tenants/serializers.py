from rest_framework import serializers
from shared.tenants.models import Tenant, Domain

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class DomainSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Domain
        fields = '__all__'