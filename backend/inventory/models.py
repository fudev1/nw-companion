from django.db import models

"""
Les `PERKS` sont liées aux items via une relation MANYTOMANY
Un item peut avoir plusieurs PERKS et une PERK peut être présente sur plusieurs ITEMS

RARITY est un attribut spécifique à chaque ITEM => FOREIGN KEY
Une table à part car c'est un attribut partagé pour plusieurs ITEMS
Evite de dupliquer les infos dans chaque enregistrement
"""

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    gear_score = models.IntegerField()
    rarity = models.ForeignKey('Rarity', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    perks = models.ManyToManyField('Perk')



class Rarity(models.Model):
    LEVEL_TYPES = [
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('epic', 'Epic'),
        ('legendary', 'Legendary'),
        ('artifact', 'Artifact'),        
    ]
    level = models.CharField(max_length=50) 


class Perk(models.Model):
    ALLOWED_ITEM_TYPES = [
        ('headwear', 'Helmet'),
        ('chestwear', 'Chest'),
        ('glove', 'Gloves'),
        ('legwaer', 'Legs'),
        ('footwear', 'Boots'),
        ('ring', 'Rings'),
        ('earswear', 'Ears'),
        ('necklace', 'Necklace'),
        ('primary_weapon', 'Primary Weapon'),
        ('secondary_weapon', 'Secondary Weapon'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    allowed_item_types = models.CharField(max_length=100, choices=ALLOWED_ITEM_TYPES)






