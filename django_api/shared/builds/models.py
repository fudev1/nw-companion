from django.db import models
from shared.characters.models import NwCharacter
from shared.users.models import TenantUser
from shared.new_world.models import NwWeapon, NwRole
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator



class NwEquipmentSet(models.Model):
    """ Set d'équipement complet NEW WORLD """
    build = models.OneToOneField('NwBuild', on_delete=models.CASCADE, related_name='equipment')

    # armure 
    head = models.JSONField(default=dict)
    chest = models.JSONField(default=dict)
    hands = models.JSONField(default=dict)
    legs = models.JSONField(default=dict)
    feet = models.JSONField(default=dict)

    # Bijoux
    amulet = models.JSONField(default=dict)
    ring = models.JSONField(default=dict)
    earring = models.JSONField(default=dict)

    # Armes (stockées séparément pour faciliter les calculs)
    primary_weapon = models.JSONField(default=dict)
    secondary_weapon = models.JSONField(default=dict)

    @property
    def calculated_gs(self):
        """Calcule le GS moyen de l'équipement"""
        # Logique de calcul à implémenter
        pass


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
    primary_weapon = models.ForeignKey(NwWeapon, on_delete=models.PROTECT, related_name='primary_weapon')
    secondary_weapon = models.ForeignKey(NwWeapon, on_delete=models.PROTECT, related_name='secondary_weapon')
    role = models.ForeignKey(NwRole, on_delete=models.PROTECT)

    # Détails des attributs
    base_attributes = models.JSONField(default=dict)  # Points de base
    """format : 
    {
        "strength": 100,
        "dexterity": 50,
        "intelligence": 5,
        "focus": 5,
        "constitution": 50,
    }
    """
    food_attributes = models.JSONField(default=dict)  # Bonus nourriture
    gear_attributes = models.JSONField(default=dict)  # Bonus équipement

    @property
    def total_strength(self):
        return(
            self.base_attributes.get('strength', 5) +
            self.food_attributes.get('strength', 0) +
            self.gear_attributes.get('strength', 0)
        )

    @property
    def total_dexterity(self):
        return(
            self.base_attributes.get('dexterity', 5) +
            self.food_attributes.get('dexterity', 0) +
            self.gear_attributes.get('dexterity', 0)
        )

    @property
    def total_intelligence(self):
        return(
            self.base_attributes.get('intelligence', 5) +
            self.food_attributes.get('intelligence', 0) +
            self.gear_attributes.get('intelligence', 0)
        )

    @property
    def total_focus(self):
        return(
            self.base_attributes.get('focus', 5) +
            self.food_attributes.get('focus', 0) +
            self.gear_attributes.get('focus', 0)
        )

    @property
    def total_constitution(self):
        return(
            self.base_attributes.get('constitution', 5) +
            self.food_attributes.get('constitution', 0) +
            self.gear_attributes.get('constitution', 0)
        )


    # Arbre compétence
    primary_weapon_skills = models.JSONField(default=dict)
    secondary_weapon_skills = models.JSONField(default=dict)

    def clean(self):
        # Vérifier le total des attributs
        total_attributes = (
            self.total_strength +
            self.total_dexterity + 
            self.total_intelligence + 
            self.total_focus + 
            self.total_constitution
        )
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