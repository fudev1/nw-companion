import discord
import os
import requests

TOKEN = os.getenv('DISCORD_TOKEN')

# intents (nécessaire pour que le bot fonctionne)
intents = discord.Intents.default()
intents.members = True # récupére les infos sur les membres

# instance du client Discord
client = discord.Client(intents=intents)

# event qui se déclenche quand le bot est prêt
@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')


@client.event
async def on_member_join(member):
    print(f'{member.name} a rejoint le serveur')
    print(f'ID: {member.id}')
    print(f'username: {member.name}')
    print(f'discriminator: {member.discriminator}')
    print(f'avatar URL: {member.avatar_url}')

#     # user_data = {
#     #     'discord_id': member.id,
#     #     'discord_username': member.name,
#     #     'discriminator': member.discriminator,
#     #     'avatar_url': str(member.avatar_url),
#     # }

#     # response = requests.post('http://localhost:8000/api/members', json=user_data)

#     # if response.status_code == 201:
#     #     print(f"User {member.name} enregistré avec succès")
#     # print(f"erreur lors de l'enregistrement: {response.status_code}")



client.run(TOKEN)
