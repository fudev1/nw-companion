from django.db import models
from django.contrib.auth.models import User

"""
Héritage multi-table
    - Chaque modèle a sa propre Table + Relation 1-1 : Parent > Enfant
    - Avoir des données à chaque sous class tout en partageant des infos générales
"""



class BaseProfile(models.Model):
    """ NOTE: Classe abstraite pour centraliser les champs communs (Empèche la création d'une table pour cette classe) """
    avatar = models.ImageField(upload_to = "avatars/", blank=True, null=True)

    class Meta: 
        abstract = True 



class MemberProfile(BaseProfile):
    """ NOTE: Profil du membre lié à l'utilisateur Django """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    discord_username = models.CharField(max_length=100, unique=True)
    discord_roles = models.ManyToManyField('Role', related_name='discord_roles')
    is_invited = models.BooleanField(default=True) # Si admin active le membre = False

    def __str__(self):
        return self.discord_username
    


class Character(BaseProfile):
    """ NOTE: Personnage en jeu créé par un utilisateur """ 
    owner = models.ForeignKey(MemberProfile, on_delete=models.CASCADE, related_name='characters')
    game_username = models.CharField(max_length=100, unique=True)
    role_in_game = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, related_name='game_roles')
    is_war_ready = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.game_username} (Owned by: {self.owner.discord_username})"



class Role(models.Model):
    """ NOTE: Roles attribués au membres (discord / jeu) """ 
    ROLE_TYPES = [
        ('discord', 'Discord Role'),
        ('game', 'Game Role')
    ]

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=ROLE_TYPES)

    def __str__(self): 
        return f'{self.name} ({self.type})' 



