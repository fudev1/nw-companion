from rest_framework import serializers
from .models import NwCharacter
from shared.new_world.models import NwServer, NwRegion, NwRole

class NwCharacterSerializer(serializers.ModelSerializer):
    # Champs en read only pour afficher les noms
    server_name = serializers.CharField(source='server.name', read_only=True)
    faction_name = serializers.CharField(source='faction.name', read_only=True)
    role_name = serializers.CharField(source='role.name', read_only=True)

    class Meta:
        model = NwCharacter
        fields = [
            'id', 'name', 'avatar_url', 'war_ready',
            'server', 'server_name',
            'faction', 'faction_name',
            'roles_type', 'role_name',
            'active_build',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


    def create(self, validated_data):
        # associer automatiquement l'user courant
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
