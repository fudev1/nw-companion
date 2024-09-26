from rest_framework import serializers
from .models import Character, Role, MemberProfile, CharacterRole

class CharacterSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Character
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Role
        fields = '__all__'

class MemberProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MemberProfile
        fields = '__all__'

class CharacterRoleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CharacterRole
        fields = '__all__'