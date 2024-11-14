from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=100)

class Server(Game):
    name = models.CharField(max_length=100)

class Faction(Game):
    name = models.CharField(max_length=100)
    