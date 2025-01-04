from django.db import models
from shared.users.models import TenantUser
from shared.new_world.models import NwFaction, NwServer, NwRole

class BaseCharacter(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(TenantUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

class NwCharacter(BaseCharacter):
    server = models.ForeignKey(NwServer, on_delete=models.PROTECT, related_name='characters', null=True, blank=True)
    faction = models.ForeignKey(NwFaction, null=True, blank=True, on_delete=models.PROTECT, related_name='characters') 
    roles_type = models.ForeignKey(NwRole, on_delete=models.PROTECT, related_name='characters')
    active_build = models.ForeignKey('builds.NwBuild', null=True, blank=True, on_delete=models.SET_NULL, related_name='active_for_characters')
    war_ready = models.BooleanField(default=False)

    @property
    def current_role(self):
        return self.active_build.role if self.active_build else self.roles_type
    
    @property
    def current_gs(self):
        return self.active_build.equipment.calculated_gs if self.active_build and hasattr(self.active_build, 'equipment') else 0
    
    def __str__(self):
        faction_name = self.faction.name if self.faction else "No Faction"
        server_name = self.server.name if self.server else "No Server"
        return f"{self.name} ({server_name} - {faction_name})"
    
    class Meta:
        ordering = ['server__region', 'server', 'name']

class TlCharacter(BaseCharacter):
    pass