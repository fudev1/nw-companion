from django.db import models
from shared.users.models import TenantUser


# Model de base pour les characters de tous les jeux
class BaseCharacter(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(TenantUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar_url = models.URLField(null=True, blank=True)

    # class Meta: 
    #     abstract = True
    #     unique_together = ['name', 'server']

    def __str__(self):
        return f"{self.name} ({self.user.username})"
    

# Model character pour New World
class NwCharacter(BaseCharacter):
    FACTION_CHOICES = [ 
        ('marauders', 'Marauders'),
        ('syndicate', 'Syndicate'),
        ('covenant', 'Covenant'),
    ]

    ROLES_CHOICES = [
        ('point', 'Point'),
        ('bruiser', 'Bruiser'),
        ('mage', 'Mage'),
        ('healer', 'Healer'),
        ('support', 'Support'),
        ('assassin', 'Assassin'),
    ]

    server = models.CharField(null=True, blank=True)
    faction = models.CharField(max_length=50, choices=FACTION_CHOICES)
    roles_type = models.CharField(max_length=50, choices=ROLES_CHOICES)

    # class Meta: 
    #     db_table = 'characters_nwcharacter'



# Model character pour TL
class TlCharacter(BaseCharacter):
    # ajouter les champs spécifiques pour TL plus tard
    pass 