from django.contrib import admin
from .models import NwPerk, NwRole, NwWeapon, NwArmorWeight, NwServer, NwGem, NwRegion, NwServerSet, NwFaction

@admin.register(NwWeapon)
class NwWeaponAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(NwRole)
class NwRoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(NwPerk)
class NwPerkAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['compatible_weapons', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(NwFaction)
class NwFactionAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ['name']

@admin.register(NwRegion)
class NwRegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ['name']

@admin.register(NwServer)
class NwServerAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'world_set', 'is_active']
    list_filter = ['region', 'is_active']
    search_fields = ['name']

@admin.register(NwServerSet)
class NwServerSetAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ['name']

@admin.register(NwGem)
class NwGemAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']

@admin.register(NwArmorWeight)
class NwArmorWeightAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']