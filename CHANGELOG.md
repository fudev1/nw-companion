# Changelog NW Companion

## [2025-01-04] Système de Création de Personnage

### Modèles
#### NwCharacter
- Champs principaux : name, avatar_url, war_ready
- Relations :
  - user (ForeignKey → TenantUser)
  - server (ForeignKey → NwServer)
  - faction (ForeignKey → NwFaction)
  - roles_type (ForeignKey → NwRole)
  - active_build (ForeignKey → NwBuild)

#### NwServer
- Champs : name, is_active
- Relations : 
  - region (ForeignKey → NwRegion)
  - world_set (ForeignKey → NwServerSet)
- Meta : ordering = ['region', 'name']

### API Endpoints

#### New World - Données de Référence
- `GET /api/new-world/regions/`
  ```json
  [{"id": 1, "name": "EU Central"}]
  ```
- `GET /api/new-world/servers/?region=1`
  ```json
  [{"id": 1, "name": "Abaton", "region": 1, "region_name": "EU Central"}]
  ```
- `GET /api/new-world/factions/`
  ```json
  [{"id": 1, "name": "Marauders"}]
  ```
- `GET /api/new-world/roles/`
  ```json
  [{"id": 1, "name": "Healer", "description": "...", "icon_url": "..."}]
  ```

#### Characters
- `GET /api/characters/new-world/` - Liste tous les personnages
- `GET /api/characters/new-world/search/?q=query` - Recherche publique
- `GET /api/characters/new-world/recent/` - Derniers personnages créés
- `GET /api/characters/new-world/my_characters/` - Personnages de l'utilisateur connecté
- `POST /api/characters/new-world/` - Création d'un personnage
  ```json
  {
    "name": "MonPerso",
    "server": 1,
    "faction": 1,
    "roles_type": 1,
    "war_ready": false,
    "avatar_url": "..."
  }
  ```
- `PUT /api/characters/new-world/{id}/` - Modification d'un personnage
- `DELETE /api/characters/new-world/{id}/` - Suppression d'un personnage

### Permissions
- Endpoints publics (AllowAny) :
  - Liste des régions, serveurs, factions, rôles
  - Liste des personnages, recherche
- Endpoints authentifiés (IsAuthenticated) :
  - Création/modification/suppression de personnages
  - Liste des personnages de l'utilisateur

### Structure du Projet
- Multi-tenancy avec django-tenants
- Apps Django :
  - `shared/characters/` : Gestion des personnages
  - `shared/new_world/` : Données de référence New World
  - `shared/users/` : Gestion des utilisateurs

### Migrations
- Migration initiale pour les modèles de base
- Migration pour les relations entre personnages et données de référence
