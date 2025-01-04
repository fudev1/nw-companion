from django.db import models
from shared.users.models import TenantUser
from shared.new_world.models import NwFaction, NwServer, NwRole


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

    # ROLES_CHOICES = [
    #     ('point', 'Point'),
    #     ('bruiser', 'Bruiser'),
    #     ('mage', 'Mage'),
    #     ('healer', 'Healer'),
    #     ('support', 'Support'),
    #     ('assassin', 'Assassin'),
    # ]

    server = models.ForeignKey(NwServer, on_delete=models.PROTECT, related_name='characters', null=True, blank=True)
    old_faction = models.CharField(max_length=50, choices=FACTION_CHOICES, null=True)  # Ancien champ
    faction = models.ForeignKey(NwFaction, null=True, on_delete=models.PROTECT, related_name='characters')  # Nouveau champ
    new_faction = models.ForeignKey(NwFaction, null=True, blank=True, on_delete=models.PROTECT, related_name='characters')
    roles_type = models.ForeignKey(NwRole, on_delete=models.PROTECT, related_name='characters')
    active_build = models.ForeignKey('builds.NwBuild', null=True, blank=True, on_delete=models.SET_NULL, related_name='active_for_characters')
    war_ready = models.BooleanField(default=False)

    @property
    def current_role(self):
        return self.active_build.role if self.active_build else None
    
    @property
    def current_gs(self):
        return self.active_build.calculated_gs if self.active_build else 0
    
    def __str__(self):
        return f"{self.name} ({self.server.name} - {self.faction.name}) | {self.user.username})"



# Model character pour TL
class TlCharacter(BaseCharacter):
    # ajouter les champs spécifiques pour TL plus tard
    pass 