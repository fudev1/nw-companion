from django.db import models
from django.contrib.auth.models import User


class MemberProfile(models.Model):
    """ profil d'un membre lié à l'utilisateur Django et au Discord """
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    discord_id = models.CharField(max_length=50, unique=True)
    discord_username = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    avatar_url = models.URLField(max_length=500, null=True, blank=True)
    discriminator = models.CharField(max_length=4)
    joined_at = models.DateTimeField(null=True, blank=True)

    #todo: Ajouter les rôles au `user_data` envoyé par le bot pour les recevoir ici
    discord_roles = models.ManyToManyField('roles.DiscordRole', related_name='discord_roles', blank=True,)

    def __str__(self):
        return f'{self.discord_username}#{self.discriminator} (User: {self.user.username if self.user else 'Invité'})'
