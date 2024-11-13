from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class CharacterCreateUpdateSerializer(serializers.ModelSerializer):
    """
    serializer pour create ou update un Character
    """
    class Meta:
        model = Character
        fields = [
            'name',
            'gear_score',
            'class_type',
            'faction',
        ]
        read_only_fields = ['id']

    def validate_gear_score(self, value):
        if value < 1 : 
            raise serializers.ValidationError('GS must be at least 1')
        return value
    

class CharacterDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Character
        fiels = [
            'id',
            'name',
            'gear_score',
            'class_type',
            'faction',
            'created_at',
            'updated_at',
            
        ]