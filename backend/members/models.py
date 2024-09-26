from django.db import models
from django.contrib.auth.models import User
from inventory.models import Item

"""
    => Un `Profile` est un membre Discord 
        🔸 C'est un compte "invité" qui est une copie de l'utilisateur discord (sans droit)
        🔸 Un user discord peut créer son compte et c'est le memberprofile qui sera lié à l'user django
        🔸 Il peut avoir plusieurs rôles liés à Discord (Management, Staff, Recruiter, etc)
        🔸 Une image comme avatar pour son profil (à mon avis ce sera récup de Discord)
        🔸 Associé au compte Discord (id, pseudo ..)

        |  TOTO (utilisateur discord) est un membre de la compagnie
        |  il a le rôle de Recruiter mais ça ne doit pas influencer sur le personnage du jeu

    => Un `Character` est un personnage dans le jeu liés au `Membre` 
        🔸 Il peut avoir un ou plusieurs Rôles (healer, bruiser, archer)
        🔸 Son rôle pourrait changer, si il souhaite se respécialiser 
        🔸 Son role est associé à un équipement (avec ses stats)
        🔸 Une image comme avatar (pour le visuel de son perso)
        🔸 Des infos sur le personnage (pseudo, war ready, level, etc)
        🔸 Un inventaire (uniquement la tenue pour vérifier si il est war ready)

        |  TOTORITO (personnage de jeu lié à TOTO) 
        |  peut sauvegarder plusieurs rôles avec son équipement spécifique et choisir lequel est prioritaire
        |  Permet de pouvoir switcher entre les rôles en fonction d'une situation (war, pve, etc)

    => `Role` représente les rôles disponibles (discord / game)

"""


class BaseProfile(models.Model):
    """ NOTE: Classe abstraite pour centraliser les champs communs (Empèche la création d'une table pour cette classe) """
    avatar = models.ImageField(upload_to = "avatars/", blank=True, null=True)

    class Meta: 
        abstract = True 



class MemberProfile(BaseProfile):
    """ 
    Profil du membre lié à l'utilisateur Django 
    A voir si je garde le BaseProfile qui donne accès à l'avatar pour les deux autres models ou pas
    Si `user` est null => il s'agit d'un user invité = n'a pas créé de compte sur le site
    """
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    # avatar = models.ImageField(upload_to = "avatars/", blank=True, null=True)
    discord_id = models.CharField(max_length=50, unique=True)
    discord_username = models.CharField(max_length=100, unique=True)
    discord_roles = models.ManyToManyField('Role', related_name='discord_roles', blank=True)
    is_invited = models.BooleanField(default=True) # True = phase d'invitation, False = membre confirmé


    def __str__(self):
        return f'{self.discord_username} (User: {self.user.username if self.user else 'Invité'})'


class Character(BaseProfile):
    """
    Personnage en jeu créé par un utilisateur ou membre Discord
    Le propriétaire peut être soit un invité (MemberProfile) soit un utilisateur avec un compte Django
    """
    pseudo_in_game = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(MemberProfile, on_delete=models.CASCADE, related_name='characters')
    active_role = models.ForeignKey('CharacterRole', on_delete=models.SET_NULL, null=True, blank=True, related_name='active_characters')
    
    def __str__(self):
        return f"{self.pseudo_in_game} (Owned by: {self.owner.discord_username})"


class CharacterRole(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='roles')
    role = models.ForeignKey('Role', limit_choices_to={'type': 'game'} ,on_delete=models.CASCADE, null=True, blank=True)
    is_war_ready = models.BooleanField(default=False)
    gear_score = models.IntegerField()
    headwear = models.ForeignKey('inventory.Item', on_delete=models.SET_NULL, null=True, related_name="headwear_roles")
    chestwear = models.ForeignKey('inventory.Item', on_delete=models.SET_NULL, null=True, related_name="chestwear_roles")
    gloves = models.ForeignKey('inventory.Item', on_delete=models.SET_NULL, null=True, related_name="gloves_roles")
    legwear = models.ForeignKey('inventory.Item', on_delete=models.SET_NULL, null=True, related_name="legwear_roles")
    footwear = models.ForeignKey('inventory.Item', on_delete=models.SET_NULL, null=True, related_name="footwear_roles")
    earswear = models.ForeignKey('inventory.Item', on_delete=models.SET_NULL, null=True, related_name="earswear_roles")
    rings = models.ForeignKey('inventory.Item', on_delete=models.SET_NULL, null=True, related_name="rings_roles")
    neclace = models.ForeignKey('inventory.Item', on_delete=models.SET_NULL, null=True, related_name="necklace_roles")
    primary_weapon = models.ForeignKey('inventory.Item', on_delete=models.SET_NULL, null=True, related_name="primary_weapon_roles")
    secondary_weapon = models.ForeignKey('inventory.Item', on_delete=models.SET_NULL, null=True, related_name="secondary_weapon_roles")

    def __str__(self):
        return f'{self.character.pseudo_in_game} - {self.role.name} ({"War Ready" if self.is_war_ready else "Not War Ready"})'



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



