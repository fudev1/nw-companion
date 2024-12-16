https://discord.com/oauth2/authorize?access_type=offline&client_id=1197274411728904192&prompt=none&redirect_uri=https%3A%2F%2Fclerk.tlgm.app%2Fv1%2Foauth_callback&response_type=code&scope=guilds+guilds.members.read+identify+email&state=puaqkmf3pm5r91qw8yy7l4qgf11n2yvyq1yq1tyg


## 1. Structure des Modèles

1. Finaliser les modèles backend :

- User Discord (TenantUser pour simplifier, avec les champs nécessaires).
- CharacterBase et les sous-classes (NewWorldCharacter, ThronesCharacter).
- Tenant (Tenant comme base commune, NewWorldCompany pour New World, etc.). 
- Toute relation pertinente entre Character et Tenant :

        Exemple : FK pour owner, M2M pour members.

2. Migration des schémas :

- Créer les migrations pour les nouveaux modèles.
- Vérifier que tout s’aligne bien avec django-tenants et tenant_users.

## 2. API Endpoints
Créer les endpoints essentiels pour les fonctionnalités suivantes :

1. Authentification Discord (Frontend pourra se connecter et récupérer les infos d’un user) :

- Endpoint de login via OAuth2 Discord.
- Endpoint pour récupérer les infos de l’utilisateur connecté (/api/me).

2. Gestion des Personnages :

- Créer un personnage (POST /api/characters/).
- Liste des personnages d’un user (GET /api/characters/?user_id=).

3. Gestion des Compagnies :

- Créer une compagnie (POST /api/companies/).
- Associer un personnage en tant que propriétaire (owner) lors de la création.
- Lister les compagnies (GET /api/companies/).

4. Provisionnement Tenant :

- Endpoint pour déclencher provision_tenant lors de la création d’une compagnie.

5. Filtrage :

- Ajouter les filtres essentiels : jeux, serveurs, factions, etc.

## 3. Test Rapide

- Utiliser Postman/Swagger pour tester les endpoints et vérifier leur bon fonctionnement.
- Mocker les données si nécessaire pour tester.


# FRONTEND
## 1. Authentification

- Mettre en place la logique d’authentification côté frontend :
- Bouton "Login" qui redirige vers Discord pour l'authentification.
- Récupérer et stocker le token JWT et les infos utilisateur.
- Afficher les données utilisateur :

        Si connecté, afficher le profil utilisateur (nom Discord, avatar).

## 2. Navigation

- Finaliser la navigation en fonction des différents contextes :
- Site principal (home).
- New World (liens spécifiques).
- Tenant (liens spécifiques).
- Intégrer les liens dynamiques selon le contexte.

## 3. Personnages
 
- Ajouter un formulaire pour créer un personnage :

        Exemple : Formulaire pour NewWorldCharacter.
- Envoyer les données via un POST /api/characters/.
- Afficher la liste des personnages de l’utilisateur connecté.

## 4. Création de Compagnie

- Ajouter un formulaire pour créer une compagnie :

        Exemple : Formulaire pour NewWorldCompany.
- Appeler /api/companies/ avec les infos nécessaires.
- Lier le personnage sélectionné comme propriétaire.
- Rediriger l’utilisateur vers le tenant créé une fois la compagnie validée.

## 5. Design Basique

- Appliquer les thèmes principaux (site principal, New World, Tenant).
- Ajouter un minimum de style pour une présentation propre.

# OBJECTIF FINAL DU MVP

- Authentification fonctionnelle.
- Création de personnages et compagnies.
- Navigation dynamique entre les contextes.
- Provisionnement de tenants opérationnel.
