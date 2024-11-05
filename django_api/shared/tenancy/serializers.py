from rest_framework import serializers
from shared.tenancy.models import Company, Domain

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class DomainSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Domain
        fields = '__all__'