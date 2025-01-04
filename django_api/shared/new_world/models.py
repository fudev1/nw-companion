from django.db import models

class NwFaction(models.Model):
    name = models.CharField(max_length=20)
    # slug = models.SlugField(unique=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class NwRegion(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class NwServerSet(models.Model):
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class NwServer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    region = models.ForeignKey(NwRegion, on_delete=models.PROTECT)
    world_set = models.ForeignKey(NwServerSet, on_delete=models.PROTECT, null=True)
    is_active = models.BooleanField(default=True)

    class Meta: 
        ordering = ['region', 'name']

    def __str__(self):
        return f"{self.name} ({self.region.name})"
    
    

class NwWeapon(models.Model):
    CATEGORY_CHOICES = [
        ('one_handed', 'One-Handed'),
        ('two_handed', 'Two-Handed'),
        ('ranged', 'Ranged'),
        ('magical', 'Magical'),
    ]

    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta: 
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
    

class NwRole(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta: 
        ordering = ['name']

    def __str__(self):
        return self.name
    
class NwArmorWeight(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class NwPerk(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    compatible_weapons = models.ManyToManyField(NwWeapon, blank=True)

    def __str__(self):
        return self.name
    
class NwGem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    