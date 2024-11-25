# Structure du Projet Angular 18 - Version Standalone

```
src/
├── app/
│   ├── core/           # Services singleton, guards, interceptors
│   ├── shared/         # Composants, directives, pipes réutilisables
│   ├── features/       # Modules fonctionnels
│   │   ├── main/       # Site principal
│   │   ├── dashboard/  # Interface d'administration
│   │   └── tenant/     # Sites spécifiques aux guildes
│   └── layouts/        # Composants de mise en page
├── assets/             # Images, fonts, etc.
└── styles/             # Styles globaux et thèmes
```

## Points Clés de l'Architecture

1. **Architecture Modulaire**
   - Composants standalone
   - Lazy loading pour chaque feature
   - Séparation claire des responsabilités

2. **Multi-tenant**
   - Layouts spécifiques pour chaque type de guilde
   - Thèmes distincts (New World, TL, WoW)
   - Routing dynamique basé sur le tenant

3. **Sécurité**
   - Guards pour le dashboard
   - Interceptors pour la gestion des tenants
   - Authentication et autorisation

4. **Performance**
   - Lazy loading
   - Composants standalone
   - Optimisation des bundles

5. **Maintenabilité**
   - Structure claire et évolutive
   - Séparation des préoccupations
   - Documentation intégrée


# Core Module Structure

```
core/
├── guards/
│   └── auth.guard.ts
├── interceptors/
│   └── tenant.interceptor.ts
├── services/
│   ├── auth.service.ts
│   ├── tenant.service.ts
│   └── company.service.ts
├── models/
│   ├── user.model.ts
│   ├── company.model.ts
│   └── tenant.model.ts
└── constants/
    └── tenant-types.ts
```

Ce dossier contient les éléments essentiels et singleton de l'application :
- Guards pour la sécurité
- Interceptors pour la gestion des requêtes
- Services partagés
- Modèles de données
- Constants


# Layouts Structure

```
layouts/
├── main-layout/
│   ├── components/
│   │   ├── header/
│   │   │   ├── navigation/
│   │   │   └── login-button/
│   │   └── footer/
│   └── main-layout.component.ts
├── dashboard-layout/
│   ├── components/
│   │   ├── sidebar/
│   │   └── topbar/
│   └── dashboard-layout.component.ts
└── tenant-layout/
    ├── new-world-layout/
    ├── tl-layout/
    └── wow-layout/
```

Gestion des différentes mises en page :
- Main : Layout principal du site
- Dashboard : Layout de l'interface d'administration
- Tenant : Layouts spécifiques pour chaque type de guilde/compagnie

# Shared Module Structure

```
shared/
├── components/
│   ├── buttons/
│   ├── cards/
│   ├── forms/
│   └── modals/
├── directives/
├── pipes/
└── utils/
```

Ce dossier contient tous les éléments réutilisables dans l'application :
- Components UI réutilisables
- Directives communes
- Pipes personnalisés
- Fonctions utilitaires

# Features Module Structure

```
features/
├── main/
│   ├── home/
│   │   ├── components/
│   │   │   ├── hero-section/
│   │   │   └── features-section/
│   │   └── home.component.ts
│   ├── new-world/
│   │   ├── components/
│   │   │   ├── company-creation/
│   │   │   ├── companies-showcase/
│   │   │   └── features-showcase/
│   │   └── new-world.component.ts
│   ├── tl/
│   ├── pricing/
│   └── contact/
├── dashboard/
│   ├── profile/
│   ├── company-management/
│   │   ├── new-world/
│   │   ├── tl/
│   │   └── wow/
│   └── settings/
└── tenant/
    ├── new-world/
    │   ├── components/
    │   ├── styles/
    │   └── new-world-tenant.component.ts
    ├── tl/
    └── wow/
```

Structure des fonctionnalités principales :
- Main : Site principal public
- Dashboard : Interface d'administration
- Tenant : Sites spécifiques aux guildes/compagnies


# Styles Structure

```
styles/
├── base/
│   ├── _reset.scss
│   ├── _typography.scss
│   └── _variables.scss
├── layouts/
│   ├── _main.scss
│   ├── _dashboard.scss
│   └── _tenant.scss
├── themes/
│   ├── new-world/
│   ├── tl/
│   └── wow/
└── main.scss
```

Organisation des styles :
- Base : Styles fondamentaux
- Layouts : Styles spécifiques aux layouts
- Themes : Styles spécifiques aux différents tenants