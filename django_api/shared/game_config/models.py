from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Server(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='servers')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.game.name})"

class Faction(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='factions')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.game.name})"




"""
new_world = Game.objects.create(name="New World")

# Ajouter des serveurs à New World
server_1 = Server.objects.create(game=new_world, name="Server 1")
server_2 = Server.objects.create(game=new_world, name="Server 2")

# Ajouter des factions à New World
faction_1 = Faction.objects.create(game=new_world, name="Marauders")
faction_2 = Faction.objects.create(game=new_world, name="Syndicate")

# Récupérer les serveurs de New World
servers = new_world.servers.all()

# Récupérer les factions de New World
factions = new_world.factions.all()
"""