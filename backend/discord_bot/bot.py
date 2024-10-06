import discord
import os
import requests
from discord.ext import commands

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
async def get_member(ctx, member_id: int):
    guild = ctx.guild
    member = guild.get_member(member_id)
    if member:
        await ctx.send(f"username: {member.name}, avatar: {member.display_avatar.url}")
    else: 
        await ctx.send("member not found")


@client.command()
async def get_all_members_command(ctx):
    guild = ctx.guild
    members_info = await get_all_members(guild)
    
    for member in members_info:
        await ctx.send(f"username: {member['name']}, avatar: {member['avatar_url']}")

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
