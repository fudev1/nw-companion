from rest_framework import serializers
from .models import Character, Role, MemberProfile, CharacterRole, User


"""
Pour les Hyperliens : 
🔸Membre -> Personnages (un membre peut avoir plusieurs personnages)
🔸Personnage -> Rôles (un personnage peut avoir plusieurs rôles : healer, bruiser, etc)
🔸Rôle -> Équipement (chaque rôle est associé à un équipement)
🔸Rôle Discord -> Membres (un rôle Discord peut être attribué à plusieurs membres)
"""

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    roles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='role-detail')
    class Meta: 
        model = Character
        fields = ['url', 'pseudo_in_game', 'owner', 'active_role', 'roles']



class RoleSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta: 
        model = Role
        fields = ['url', 'name', 'type', 'types']



class MemberProfileSerializer(serializers.HyperlinkedModelSerializer):
    characters = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='character-detail')
    discord_roles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='role-detail')
    
    class Meta: 
        model = MemberProfile
        fields = ['url', 'user', 'discord_id', 'discord_username', 'discord_roles', 'is_invited', 'characters']



class CharacterRoleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CharacterRole
        fields = '__all__'