from rest_framework import serializers
from .models import NwCompany

class NwCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = NwCompany
        fields = '__all__'

