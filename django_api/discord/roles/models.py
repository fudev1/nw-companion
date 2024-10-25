from django.db import models


class DiscordRole(models.Model):
    """ Tous les rôles récupéré de Discord """
    
    ROLE_TYPES = [
        ('discord', 'Discord Role'),
        ('new_world', 'New World')
    ]
    name = models.CharField(max_length=50)
    description = models.TextField( blank=True)
    role_type = models.CharField(max_length=50, choices=ROLE_TYPES)

    def __str__(self):
        return f'{self.name} ({self.role_type})'
