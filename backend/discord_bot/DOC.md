**Intents**

- S'assurer que les `intents`sont activés dans le portail développeur, sinon le bot ne pourra pas récupérer les infos (ex: members)
- Pour récupérer des infos => Utiliser des `intents` appropriés


'discriminator' => Correspond aux 4 chiffres après le `username` du membre. 
Permet de différencier les utilisateurs qui ont le même nom. (user#1234)


# Mapper les champs Discord -> API
Pas obliger de faire correspondre les KEY du models avec ceux qui sont envoyé par le bot. 
Par exemple :   `discord_username` (dans mon models) et discord envoie la key : `username`
                -> il faut mapper correctement pour faire correspondre les deux lors du traitements des données

```python
user_data = {
    'discord_id': member.id,
    'discord_username': member.name,  # Assigner "name" (username) de Discord au champ "discord_username"
    'discriminator': member.discriminator,
    'avatar_url': str(member.avatar_url),
}

response = requests.post('http://ton_api_django_url/api/users/', json=user_data)
```

# Lister tous les attributs et méthodes d'un objet : 

```python
@bot.event
async def on_member_join(member)
    print(dir(member))
```


# Objet `guild`
=> Informations des tous les membres `guild.member` ou `guild.get_member()`

# object Member :

```json
['__annotations__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_avatar', '_avatar_decoration_data', '_client_status', '_copy', '_flags', '_from_client_user', '_from_message', '_get_channel', '_permissions', '_presence_update', '_roles', '_state', '_try_upgrade', '_update', '_update_from_message', '_update_inner_user', '_user', 'accent_color', 'accent_colour', 'activities', 'activity', 'add_roles', 'avatar', 'avatar_decoration', 'avatar_decoration_sku_id', 'ban', 'banner', 'bot', 'color', 'colour', 'create_dm', 'created_at', 'default_avatar', 'desktop_status', 'discriminator', 'display_avatar', 'display_icon', 'display_name', 'dm_channel', 'edit', 'fetch_message', 'flags', 'get_role', 'global_name', 'guild', 'guild_avatar', 'guild_permissions', 'history', 'id', 'is_on_mobile', 'is_timed_out', 'joined_at', 'kick', 'mention', 'mentioned_in', 'mobile_status', 'move_to', 'mutual_guilds', 'name', 'nick', 'pending', 'pins', 'premium_since', 'public_flags', 'raw_status', 'remove_roles', 'request_to_speak', 'resolved_permissions', 'roles', 'send', 'status', 'system', 'timed_out_until', 'timeout', 'top_role', 'typing', 'unban', 'voice', 'web_status']
```

## Attributs et Méthodes Utiles de member
- `name` : Le nom d'utilisateur du membre.
- `display_name` : Le nom affiché (qui peut être un pseudonyme spécifique au serveur).
- `id` : L'ID unique de l'utilisateur (utilisé pour identifier un membre).
- `avatar` : Retourne un objet Asset représentant l'avatar du membre.
- `display_avatar` : L'avatar affiché par le membre (avatar global ou spécifique à un serveur).
- `joined_at` : La date à laquelle le membre a rejoint le serveur.
- `roles` : Liste des rôles attribués au membre dans ce serveur.
- `guild` : Retourne l'objet Guild (le serveur auquel le membre appartient).
- `guild_permissions` : Retourne les permissions du membre sur le serveur.
- `status` : Le statut du membre (en ligne, hors ligne, etc.).
- `is_on_mobile` : Booléen indiquant si le membre est connecté via un appareil mobile.
- `bot` : Booléen indiquant si le membre est un bot ou un utilisateur humain.

## Exemples de Méthodes que tu peux Utiliser
- `add_roles()` : Permet d'ajouter un rôle à un membre.
- `kick()` : Permet de kicker un membre du serveur.
- `ban()` : Permet de bannir un membre du serveur.
- `send()` : Permet d'envoyer un message en DM à ce membre.
- `edit()` : Modifier les informations du membre, par exemple son pseudonyme.

