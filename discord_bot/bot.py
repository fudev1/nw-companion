import discord
import os
import requests
from discord.ext import commands
from discord import Embed
import json
import http.client

http.client.HTTPConnection.debuglevel = 1


TOKEN = os.getenv('DISCORD_TOKEN')
BACKEND_URL = 'http://django-nw-companion:8000'


# Identifiants du bot pour obtenir un JWT
BOT_USERNAME = os.getenv('BOT_USERNAME')
BOT_PASSWORD = os.getenv('BOT_PASSWORD')

# intents (nécessaire pour que le bot fonctionne)
intents = discord.Intents.default()
intents.members = True # récupére les infos sur les membres
intents.message_content = True # permet au bot de lire les messages de commande

# instance du client Discord
# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)



# Obtenir un token JWT
def get_jwt_token():
    data = {
        'username': BOT_USERNAME,
        'password': BOT_PASSWORD
    }
    print("Données envoyées pour obtenir le token JWT:", data)
    
    response = requests.post(f"{BACKEND_URL}/token/", data=data)
    if response.status_code == 200:
        return response.json().get('access')
    else:
        print("erreur lors de l'obtention du token", response.status_code, response.text)
        return None



# event qui se déclenche quand le bot est prêt
@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')
    print(f"BOT_USERNAME: {BOT_USERNAME}")
    print(f"BOT_PASSWORD: {BOT_PASSWORD}")


@client.event
async def on_member_join(member):
    print(f'{member.name} a rejoint le serveur')
    print(f'ID: {member.id}')
    print(f'username: {member.name}')
    print(f'discriminator: {member.discriminator}')
    if member.avatar is not None: 
        print(f'avatar URL: {member.display_avatar.url}')
    else: 
        print("pas d'avatar personnalisé, avatar par défaut de Discord utilisé")

#     # user_data = {
#     #     'discord_id': member.id,
#     #     'discord_username': member.name,
#     #     'discriminator': member.discriminator,
#     #     'avatar_url': str(member.avatar_url),
#     # }

#     # response = requests.post('{BACKEND_URL}/api/members/', json=user_data)

#     # if response.status_code == 201:
#     #     print(f"User {member.name} enregistré avec succès")
#     # print(f"erreur lors de l'enregistrement: {response.status_code}")


@client.command()
async def get_all_members_count(ctx):
    
    guild = ctx.guild
    members_count = len(guild.members)
    await ctx.send(f"il y a {members_count} users sur ce discord")



@client.command()
async def get_member(ctx, member_id: int):
    guild = ctx.guild 
    member = guild.get_member(member_id)
    if member:
        member_info = {
            "discord_id": member.id,
            "discord_username": member.name,
            "discriminator": member.discriminator,
            "display_name": member.display_name,
            "avatar_url": str(member.display_avatar.url),
            "joined_at": member.joined_at.isoformat() if member.joined_at else None
        }
        print(json.dumps(member_info, indent=4))
        jwt_token = get_jwt_token()

        if jwt_token:
            # Info coté docker cli
            print("Données envoyées:", json.dumps(member_info, indent=4))
 
            response = requests.post('http://django-nw-companion:8000/api/members/', headers={'Authorization': f'Bearer {jwt_token}'}, json=member_info)
            if response.status_code == 201:
                await ctx.send(f"Informations de l'utilisateur {member.name} envoyées au backend avec succès.") # DISCORD
            else:
                await ctx.send(f"Erreur lors de l'envoi des informations: {response.status_code} - {response.text}")
                print(f"Erreur lors de l'envoi des informations: {response.status_code} - {response.text}")
        else:
            await ctx.send("Erreur: Le bot n'a pas eu l'obtention du token JWT.")
    else:
        await ctx.send("Membre non trouvé.")



# print JSON (all membre)

@client.command()
async def print_get_all_members(ctx):
    guild = ctx.guild
    members_info = await get_all_members(guild)
    print(json.dumps(members_info, indent=4))

# print tous les attributs de l'object d'un membre
@client.command()
async def print_member_object(ctx, member_id:int):
    guild = ctx.guild
    member = guild.get_member(member_id)
    if member:
        print(dir(member))
        await ctx.send("Les attributs de l'objet membre ont été affichés dans la console.")
    else: 
        await ctx.send("Membre non trouvé.")

async def get_all_members(guild):
    members = guild.members
    members_info = []
    for member in members: 
        members_info.append({
            "id": member.id,
            "name": member.name,
            "display_name": member.display_name,
            "avatar_url": str(member.display_avatar.url),
            "joined_at": member.joined_at.isoformat() if member.joined_at else None
        })
    return members_info


client.run(TOKEN)
