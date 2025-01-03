from django.db import models
from shared.characters.models import NwCharacter
from shared.users.models import TenantUser
from django.core.exceptions import ValidationError



class BaseBuild(models.Model):
    # Infos de base Build
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(TenantUser, on_delete=models.CASCADE, related_name="%(class)s_builds")
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)

    # Stats Social
    likes_count = models.IntegerField(default=0)
    views_count = models.IntegerField(default=0)

    # Times
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True
        ordering = ['-likes_count', '-created_at']

    def __str__(self):
        return f"{self.name} by {self.creator.username}"



class NwBuild(BaseBuild):
    # Build pour NW
    character = models.ForeignKey(NwCharacter, on_delete=models.CASCADE, related_name='builds')

    # Config 
    primary_weapon = models.CharField(max_length=50)
    secondary_weapon = models.CharField(max_length=50)
    role_type = models.CharField(max_length=20)

    # Attributs des points
    strength = models.IntegerField(default=5)
    dexterity = models.IntegerField(default=5)
    intelligence = models.IntegerField(default=5)
    focus = models.IntegerField(default=5)
    constitution = models.IntegerField(default=5)

    # Arbre compétence
    primary_weapon_skills = models.JSONField(default=dict)
    secondary_weapon = models.JSONField(default=dict)

    def clean(self):
        # Vérifier le total des attributs
        total_attributes = (self.strength + self.dexterity + self.intelligence + self.focus + self.constitution)
        if total_attributes > 500:
            raise ValidationError("le total des points ne peut pas dépasser 500 points")
        
    class Meta(BaseBuild.Meta):
        verbose_name = "New World Build"
        verbose_name_plural = "New World Builds"
    
    def __str__(self):
        return f'{self.name} ({self.primary_weapon}/{self.secondary_weapon})'
    

class BuildLike(models.Model):
    """Modèle pour gérer les likes des builds (commun à tous les types)"""
    # On utilisera GenericForeignKey car les likes peuvent être sur n'importe quel type de build
    from django.contrib.contenttypes.fields import GenericForeignKey
    from django.contrib.contenttypes.models import ContentType
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    build = GenericForeignKey('content_type', 'object_id')
    
    user = models.ForeignKey(TenantUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('content_type', 'object_id', 'user')
        indexes = [
            models.Index(fields=['content_type', 'object_id'])
        ]