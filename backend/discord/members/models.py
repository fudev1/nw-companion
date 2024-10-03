from django.db import models
from django.contrib.auth.models import User


class MemberProfile(models.Model):
    """ profil d'un membre lié à l'utilisateur Django et au Discord """
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    discord_id = models.CharField(max_length=50, unique=True)
    discriminator = models.CharField(max_length=4)
    discord_username = models.CharField(max_length=100)
    discord_roles = models.ManyToManyField('roles.DiscordRole', related_name='discord_roles', blank=True,)
    avatar_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.discord_username}#{self.discriminator} (User: {self.user.username if self.user else 'Invité'})'
