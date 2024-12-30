from rest_framework import serializers
from .models import NwCharacter, TlCharacter
from shared.users.serializers import TenantUserSerializer
from shared.users.models import TenantUser

class NwCharacterSerializer(serializers.ModelSerializer):
    # user = TenantUserSerializer(read_only=True)

    class Meta:
        model = NwCharacter
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        # associer automatiquement l'user courant
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
