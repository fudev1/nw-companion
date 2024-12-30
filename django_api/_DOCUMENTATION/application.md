# Parties publique (schema Public) VS Parties privées (schema Tenants)


PUBLIC = Tout ce qui sera accessible dans la partie publique (site principale)
- Discord User (compte discord de l'utilisateur)
- Tenants (pouvoir lister tous les tenants dans public)

- New_World/Company (pouvoir lister toutes les compagnies new world)
- New_World/Character (pouvoir lister les perso, ex: les nouveau perso créés, etc)
- New_World/Wars (le but c'est de pouvoir lister les prochaines wars avec les win/loose. Chaque Tenant enregistrera sur son dashboard un nouvel évent war avec des infos et ça aurait été bien de pouvoir récupérer certaines info en public et garder d'autre en privé ?)
- New_World/Server (lister des serveur)
- New_World/Faction (liste des factions)
- New_World/Build (pour les build des perso)

- Thrones_Liberty/.... (avoir la même structure pour ce jeu)

- Base/Character (pour les base ? Genre CharacterBase, tout ce qui serait partagé entre les app ?)
- Base/Game (pour les type de jeu ?)
- Base/Group (pour les champs commun avec guild, companie etc ?)


PRIVE = Tout ce qui appartient aux tenant et donc dans le schema tenant (donnée isolée)
- New_World/Salaries (pour les salaires des joueurs)
- New_World/Calendar (pour la gestion des events de la companie = race, wars, opr, mutation, etc)
- New_World/ApplyRequest (pour les requests, c'est la liste des character qui veulent rejoindre la companie)
- New_World/ScoreBoard (pour les tableaux de scores des wars, résultat joueur par joueur et win / loose etc)
- New_World/Roster (pour la gestion des roster dans la companie)
- New_World/RaidPlan (pour la gestion des plan de guerre)
- New_World/Announcement (pour les announcement sur le site tenant)
et d'autre tables si nécessaire 

Si c'est une guilde pour Thrones alors il aurait les tables pour thrones ..
