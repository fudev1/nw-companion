# Architecture du Projet Guild Manager

```
src/
├── app/
│   ├── core/                    # Éléments partagés globalement
│   │   ├── auth/               # Authentication globale
│   │   │   ├── services/
│   │   │   └── guards/
│   │   ├── layout/             # Layout components partagés
│   │   │   ├── main-header/    # Header avec logo + auth
│   │   │   └── main-footer/
│   │   └── services/           # Services globaux
│   │       ├── user.service.ts
│   │       └── theme.service.ts
│   │
│   ├── games/                  # Modules spécifiques aux jeux
│   │   ├── new-world/
│   │   │   ├── components/     # Components spécifiques NW
│   │   │   │   ├── header/     # Header contextualisé NW
│   │   │   │   └── navigation/ # Navigation NW
│   │   │   ├── features/       # Features spécifiques NW
│   │   │   │   ├── company-creation/
│   │   │   │   ├── companies-list/
│   │   │   │   └── dashboard/  # Gestion compagnie
│   │   │   ├── models/
│   │   │   └── services/
│   │   │
│   │   ├── wow/               # Même structure pour WoW
│   │   └── tl/                # Même structure pour TL
│   │
│   ├── tenant/                # Gestion des sites tenants
│   │   ├── new-world/
│   │   │   ├── components/    # Components tenant NW
│   │   │   ├── layout/       # Layout spécifique tenant NW
│   │   │   └── features/     # Features du tenant
│   │   ├── wow/
│   │   └── tl/
│   │
│   ├── landing/              # Site principal
│   │   ├── components/
│   │   ├── features/
│   │   │   ├── home/
│   │   │   ├── pricing/
│   │   │   └── about/
│   │   └── layout/
│   │
│   └── shared/              # Components/services réutilisables
│       ├── components/
│       ├── directives/
│       └── pipes/
│
├── assets/
└── styles/
    ├── base/
    ├── games/              # Styles spécifiques aux jeux
    │   ├── new-world/
    │   ├── wow/
    │   └── tl/
    └── tenant/            # Styles spécifiques aux tenants
```

## Points Clés de l'Architecture

1. **Authentication Globale**
   - Gestion centralisée dans le core
   - État de connexion partagé entre tous les contextes
   - Guards et interceptors globaux

2. **Séparation par Contexte**
   - Landing : Site principal marketing
   - Games : Modules spécifiques par jeu
   - Tenant : Sites personnalisés des guildes

3. **Navigation Contextuelle**
   - Header global avec auth dans core
   - Navigation spécifique par jeu
   - Navigation personnalisée par tenant

4. **Routing**
   - Routes principales : guildmanager.app/*
   - Routes jeux : [game].guildmanager.app/*
   - Routes tenants : [tenant].[game].guildmanager.app/*

5. **Gestion des Styles**
   - Styles de base partagés
   - Thèmes spécifiques par jeu
   - Personnalisation par tenant

## Spécificités Techniques

1. **Core Module**
   - Authentication centralisée
   - Services partagés
   - Components de base réutilisables

2. **Games Modules**
   - Lazy loading par jeu
   - Features spécifiques au jeu
   - Dashboard de gestion intégré

3. **Tenant Module**
   - Personnalisation par guilde
   - Thèmes spécifiques
   - Fonctionnalités de gestion




src/
├── app/
│   ├── core/                           # Éléments globaux partagés
│   │   ├── auth/                       # Gestion de l'authentification
│   │   │   ├── auth.guard.ts
│   │   │   └── auth.service.ts
│   │   ├── layout/                     # Layout global
│   │   │   ├── header/
│   │   │   │   ├── header.component.ts
│   │   │   │   ├── header.component.html
│   │   │   │   └── header.component.scss
│   │   │   ├── footer/
│   │   │   │   ├── footer.component.ts
│   │   │   │   ├── footer.component.html
│   │   │   │   └── footer.component.scss
│   │   │   └── layout.component.ts
│   │   └── services/                   # Services globaux
│   │       ├── navigation.service.ts
│   │       ├── user.service.ts
│   │       └── theme.service.ts
│   │
│   ├── shared/                         # Composants réutilisables
│   │   ├── components/                 # Composants UI communs
│   │   │   ├── button/
│   │   │   │   ├── button.component.ts
│   │   │   │   ├── button.component.html
│   │   │   │   └── button.component.scss
│   │   │   ├── card/
│   │   │   │   ├── card.component.ts
│   │   │   │   ├── card.component.html
│   │   │   │   └── card.component.scss
│   │   │   ├── modal/
│   │   │   │   ├── modal.component.ts
│   │   │   │   ├── modal.component.html
│   │   │   │   └── modal.component.scss
│   │   ├── directives/
│   │   │   └── tooltip.directive.ts
│   │   └── pipes/
│   │       └── capitalize.pipe.ts
│   │
│   ├── main/                        # Site principal
│   │   ├── header/                     # Section Header
│   │   │   ├── header.component.ts
│   │   │   ├── header.component.html
│   │   │   └── header.component.scss
│   │   ├── games-list/                 # Section pour les jeux disponibles
│   │   │   ├── games-list.component.ts
│   │   │   ├── games-list.component.html
│   │   │   └── games-list.component.scss
│   │   ├── features/                   # Section fonctionnalités
│   │   │   ├── features.component.ts
│   │   │   ├── features.component.html
│   │   │   └── features.component.scss
│   │   ├── pricing/                    # Page Pricing
│   │   │   ├── pricing.component.ts
│   │   │   ├── pricing.component.html
│   │   │   └── pricing.component.scss
│   │   ├── about/                      # Page About
│   │   │   ├── about.component.ts
│   │   │   ├── about.component.html
│   │   │   └── about.component.scss
│   │   ├── login/                      # Page Login
│   │   │   ├── login.component.ts
│   │   │   ├── login.component.html
│   │   │   └── login.component.scss
│   │   ├── landing.component.ts        # Page principale
│   │   ├── landing.component.html
│   │   └── landing.component.scss
│   │
│   ├── games/                          # Pages spécifiques aux jeux
│   │   ├── new-world/                  # Sous-site New World
│   │   │   ├── header/                 # Header spécifique au jeu
│   │   │   │   ├── nw-header.component.ts
│   │   │   │   ├── nw-header.component.html
│   │   │   │   └── nw-header.component.scss
│   │   │   ├── create-company/         # Section "Créer une compagnie"
│   │   │   │   ├── create-company.component.ts
│   │   │   │   ├── create-company.component.html
│   │   │   │   └── create-company.component.scss
│   │   │   ├── top-companies/          # Section Top 5 compagnies
│   │   │   │   ├── top-companies.component.ts
│   │   │   │   ├── top-companies.component.html
│   │   │   │   └── top-companies.component.scss
│   │   │   ├── company-list/           # Liste des compagnies
│   │   │   │   ├── company-list.component.ts
│   │   │   │   ├── company-list.component.html
│   │   │   │   └── company-list.component.scss
│   │   │   ├── next-war/               # Section Prochaine guerre
│   │   │   │   ├── next-war.component.ts
│   │   │   │   ├── next-war.component.html
│   │   │   │   └── next-war.component.scss
│   │   │   ├── new-world.component.ts  # Page principale de New World
│   │   │   ├── new-world.component.html
│   │   │   └── new-world.component.scss
│   │   ├── wow/                        # Autre jeu avec structure similaire
│   │
│   ├── tenants/                        # Sites de guilde (tenant)
│   │   ├── header/                     # Header spécifique tenant
│   │   │   ├── tenant-header.component.ts
│   │   │   ├── tenant-header.component.html
│   │   │   └── tenant-header.component.scss
│   │   ├── apply/                      # Section Rejoindre la guilde
│   │   │   ├── apply.component.ts
│   │   │   ├── apply.component.html
│   │   │   └── apply.component.scss
│   │   ├── top-members/                # Section Top membres
│   │   │   ├── top-members.component.ts
│   │   │   ├── top-members.component.html
│   │   │   └── top-members.component.scss
│   │   ├── member-list/                # Liste des membres
│   │   │   ├── member-list.component.ts
│   │   │   ├── member-list.component.html
│   │   │   └── member-list.component.scss
│   │   ├── next-war/                   # Prochaine guerre
│   │   │   ├── next-war.component.ts
│   │   │   ├── next-war.component.html
│   │   │   └── next-war.component.scss
│   │   ├── tenant-home.component.ts    # Page principale d’un tenant
│   │   ├── tenant-home.component.html
│   │   └── tenant-home.component.scss
│   │
│   ├── dashboard/                      # Dashboard commun
│   │   ├── guild-management/           # Gestion de la guilde
│   │   │   ├── guild-management.component.ts
│   │   │   ├── guild-management.component.html
│   │   │   └── guild-management.component.scss
│   │   ├── character-management/       # Gestion du personnage
│   │   │   ├── character-management.component.ts
│   │   │   ├── character-management.component.html
│   │   │   └── character-management.component.scss
│   │   ├── dashboard.component.ts
│   │   ├── dashboard.component.html
│   │   └── dashboard.component.scss
│   │
│   └── app.component.ts                # Racine de l’application
│
├── assets/                             # Ressources (images, styles, etc.)
├── environments/                       # Configurations des environnements
└── main.ts                             # Entrée de l'application Angular
