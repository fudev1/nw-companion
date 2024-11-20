Dossier qui contiendrait toutes les interfaces utilisées par le projet.

user.models.ts
character.models.ts
company.models.ts

=> Cette approche me semble un peu brouillon, je pense mettre ça dans un répertoire dédié pour chaque module  
exemple : module new-world/models/user.models.ts
Dans new-world j'aurai ce genre d'architecture : 

```
new-world
  models
    user.models.ts
    character.models.ts
    company.models.ts
  services
    user.service.ts
    character.service.ts
    company.service.ts
  controllers
    user.controller.ts
    character.controller.ts
    company.controller.ts
  components
    modal/
      modal.component.ts
    button/
      button.component.ts
    user.component.ts
    character.component.ts
    company.component.ts
```
