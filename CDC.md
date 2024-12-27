# Cahier des Charges - New World Companion

## Description du Projet
New World Companion est une suite d'outils destinée aux joueurs de New World et d'autres jeux. L'application propose des fonctionnalités de gestion de personnages, de guerre, et d'intégration Discord pour améliorer l'expérience de jeu.

## Architecture Technique

### Infrastructure
- Architecture conteneurisée avec Docker
- Base de données PostgreSQL
- Réseau dédié (nwcompanion-network)
- Intégration VPS (vps-network)

### Backend (Django)
- API REST Django
- Structure modulaire par jeu
  - Module New World
    - Gestion des personnages
    - Gestion des guerres
  - Module Thrones of Liberty (en préparation)
- Système d'authentification JWT
- Intégration Discord

### Frontend (Angular)
- Architecture modulaire
  - Core : Services et composants partagés
  - Module principal (p-main)
  - Module New World (p-new-world)
  - Module Thrones of Liberty (p-thrones-liberty)
- Design System personnalisé
- Composants PrimeNG

### Bot Discord
- Intégration avec l'API Django
- Commandes personnalisées par jeu
- Système de notifications

## Fonctionnalités par Module

### Core
- Authentification utilisateur
- Gestion des profils
- Système de notifications
- Thème personnalisable
- Navigation globale

### New World
#### Gestion des Personnages
- Profils de personnages
- Gestion des builds
- Statistiques et attributs
- Équipements et armes
- Appartenance aux compagnies

#### Gestion des Guerres
- Planification des guerres
- Composition des équipes
- Statistiques de guerre
- Historique des guerres

#### Intégration Discord
- Synchronisation des profils
- Commandes de gestion des personnages
- Notifications de guerre
- Gestion des compagnies

### Thrones of Liberty
*(Module en préparation)*

## Sécurité et Performance
- Authentification JWT
- Protection CSRF
- Rate limiting
- Mise en cache
- Optimisation des requêtes
- Monitoring des performances

## Déploiement
- Environnement conteneurisé
- Configuration multi-environnements
- Sauvegarde automatique des données
- Monitoring des services
- Logs centralisés

## Évolutions Futures
- Support d'autres jeux
- API publique
- Applications mobiles
- Intégration avec d'autres plateformes
- Système de plugins
