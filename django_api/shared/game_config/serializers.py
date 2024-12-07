from rest_framework import serializers
from .models import Game, Server, Faction

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class ServerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Server
        fields = '__all__'

class FactionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Faction
        fields = '__all__'