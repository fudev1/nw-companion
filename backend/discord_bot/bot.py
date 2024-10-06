import discord
import os
import requests
from discord.ext import commands
from discord import Embed
import json

TOKEN = os.getenv('DISCORD_TOKEN')

# intents (nécessaire pour que le bot fonctionne)
intents = discord.Intents.default()
intents.members = True # récupére les infos sur les membres
intents.message_content = True # permet au bot de lire les messages de commande

# instance du client Discord
# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)

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

#     # response = requests.post('http://localhost:8000/api/members', json=user_data)

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
            "id": member.id,
            "name": member.name,
            "display_name": member.display_name,
            "avatar_url": str(member.display_avatar.url),
            "joined_at": member.joined_at.isoformat() if member.joined_at else None
        }
        print(json.dumps(member_info, indent=4))
    else:
        print("Membre non trouvé.")

@client.command()
async def print_get_all_members(ctx):
    guild = ctx.guild
    members_info = await get_all_members(guild)
    print(json.dumps(members_info, indent=4))

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
