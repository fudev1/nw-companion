from django.db import models
from django.conf import settings


# Create your models here.

class CharacterBase(models.Model):
    name = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='base_characters')
    avatar_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['name']

    def __str__(self):
        return self.name