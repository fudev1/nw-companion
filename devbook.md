# Journal de Développement - New World Companion



## Légende
- [v] Terminé
- [-] En cours
- [ ] En attente
- [x] À améliorer/refactor

## Infrastructure du projet
- [ok] Docker
- [ok] PostgreSQL
- [ok] Configuration des réseaux
- [ ] Configuration du VPS
- [ ] Monitoring
- [ ] Logs centralisés
- [ ] Sauvegarde des données

## Backend (Django)
### Core
- [ok] Structure du projet
- [ok] Configuration de base
- [ ] Configuration JWT et CSRF

### Module New World
- [ok] Structure du module
- [ ] API Characters
  - [ ] Modèle Character
  - [ ] Endpoints CRUD Character
  - [ ] Tests Characters
- [ ] API Builds
  - [ ] Modèle Build
  - [ ] Endpoints CRUD Build
  - [ ] Tests Builds
- [ ] API Wars
  - [ ] Modèle War
  - [ ] Endpoints CRUD War
  - [ ] Tests Wars
- [ ] API Companies
  - [ ] Modèle Company
  - [ ] Endpoints CRUD Company
  - [ ] Tests Companies


### [ ] Modifier le modèle `Character`
[ ] Ajouter un champ `server` (obligatoire)
[ ] Ajouter une relation unique vers `Tenant` (la compagnie dont Character est membre)
[ ] Ajouter une relation boolean `is_governor` pour indiquer si le personnage est gouverneur
[ ] Modifier la contrainte `unique_together` pour inclure le champ `server`
[ ] Ajouter un champ `avatar_url` pour stocker l'url de l'avatar du Character
[ ] Ajouter un champ active_build avec une relation FK vers `Build`
[ ] Externaliser les choix de `Factions_Choices` et `Classes_Choices` en modèles distincts

=> unique_together = éviter les doublons par utilisateur

=> Validation personnalisée qui assure qu'un Character lié à un TenantUser donné respecte certaines contraintes (ex: un character ne peut pas appartenir à deux faction différentes)

### [ ] Modifier le modèle `Tenant`
[ ] Remplacer le champs `owner` (actuellement lié à `TenantUser`) par une relation vers `Character`
[ ] Ajouter un champ `server` (obligatoire)
[ ] Ajouter une contrainte unique pour qu'il ne puisse pas y avoir deux compagnies avec le même nom sur le même serveur


### [ ] Créer le modèle `Server`
[ ] Gérer la liste des serveurs de New World 
=> Permet d'avoir une référence pour les Characters et les compagnies
=> Un Character ne peut être membre que d'une seule compagnie à la fois
=> Une compagnie ne peut avoir qu'un seul gouverneur
=> Un Character ne peut être gouverneur que d'une seule companie à la fois


### [ ] Créer le modèle `Build`
[ ] name, gear_score, character (FK vers Character)
=> Chaque Character peut avoir un Build actif
=> Chaque Character peut avoir plusieurs Builds 


## Frontend (Angular)




# TIPS : 

# `unique=true` :
- appliquer sur un seul champ
- garantit que chaque valeur pour ce champs est *unique* dans toute la db 
- ex: si on défini `name = models.CharField(max_length=100, unique=True)` alors aucun autre Character ne pourra avoir ce nom même pour un autre jeu.

# `unique_together` :
- appliquer sur une combinaison de champs
- ex : unique_together = [('name', 'owner')] => garantit qu'un même user ne peut avoir deux personnages avec le meme nom