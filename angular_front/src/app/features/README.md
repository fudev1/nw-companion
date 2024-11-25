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