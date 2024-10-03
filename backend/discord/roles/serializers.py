from rest_framework import serializers
from .models import DiscordRole

class DiscordRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscordRole
        fields = '__all__'