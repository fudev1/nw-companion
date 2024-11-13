from django.db import models
from django.conf import settings

# Create your models here.

class Character(models.Model):

    FACTION_CHOICES = [
        ('marauders', 'Marauders'),
        ('syndicate', 'Syndicate'),
        ('covenant', 'Covenant'),
    ]

    CLASS_CHOICES = [
        ('point', 'Point'),
        ('bruiser', 'Bruiser'),
        ('mage', 'Mage'),
        ('healer', 'Healer'),
        ('assassin', 'Assassin'),
    ]

    name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    gear_score = models.PositiveIntegerField(default=1)
    class_type = models.CharField(max_length=50, choices=CLASS_CHOICES, blank=True, null=True)
    faction = models.CharField(max_length=50, choices=FACTION_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='characters')

    def __str__(self):
        return f"{self.name} (GS: {self.gear_score}, {self.class_type})"

    class Meta: 
        ordering = ['name']                     # tri par nom
        unique_together = ['name', 'owner']     # un même nom de perso ne peut pas être utilisé par le même propriétaire
