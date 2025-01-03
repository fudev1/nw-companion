# Tâches à Implémenter - New World Companion

## 1. Système de Builds ⭐ (Priorité Haute)
- [ ] Modèle de Build
  - Nom du build
  - Lien avec le personnage
  - Arme principale et secondaire
  - Type d'armure
  - Attributs (force, dextérité, etc.)
  - Capacités sélectionnées
- [ ] API pour CRUD des builds
- [ ] Système de partage de builds
- [ ] Système de votes/likes sur les builds

## 2. Système de Compagnies (Guildes) 🏰
- [ ] Modèle de Company
  - Nom de la compagnie
  - Leader
  - Membres
  - Faction
  - Serveur
  - Statut de recrutement
- [ ] Gestion des membres
- [ ] Système de rôles et permissions
- [ ] Annonces de recrutement

## 3. Système de Guerres ⚔️
- [ ] Modèle de War
  - Territoire concerné
  - Compagnie attaquante
  - Compagnie défenseuse
  - Date et heure
  - Statut
  - Résultat
- [ ] Planification des guerres
- [ ] Historique des guerres
- [ ] Statistiques de guerre par compagnie

## 4. Système de Territoires 🗺️
- [ ] Modèle de Territory
  - Nom du territoire
  - Compagnie contrôlante
  - Dernière guerre
  - Taux de taxe
  - Améliorations
- [ ] Suivi des changements de contrôle
- [ ] Système d'upgrades
- [ ] Statistiques économiques

## Notes Techniques
- Implémenter dans l'ordre de priorité (Builds → Compagnies → Guerres → Territoires)
- Chaque système doit avoir :
  - Modèles Django
  - Serializers
  - ViewSets
  - Tests unitaires
  - Documentation API
  - Endpoints REST
  - Intégration avec le frontend
