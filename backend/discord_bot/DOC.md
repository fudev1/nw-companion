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