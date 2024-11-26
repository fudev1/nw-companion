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

Ce dossier contient les éléments essentiels et singleton de l'application
- Guards pour la sécurité
- Interceptors pour la gestion des requêtes
- Services partagés
- Modèles de données
- Constants