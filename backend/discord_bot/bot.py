import discord
import os

TOKEN = os.getenv('DISCORD_TOKEN')

# intents (nécessaire pour que le bot fonctionne)
intents = discord.Intents.default()

# instance du client Discord
client = discord.Client(intents=intents)

# event qui se déclenche quand le bot est prêt
@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')

client.run(TOKEN)
