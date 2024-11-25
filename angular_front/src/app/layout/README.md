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