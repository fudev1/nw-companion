Séparation des préoccupations de l'application
Core : composants critiques à la structure de l'application, services globaux, ...

- CoreModule: 
Contient les services globaux (comme l'authentification), les composants de navigation (ex. navbar), et généralement tout ce qui ne doit être chargé qu'une seule fois. C'est le "cœur" de ton application.


- MODULE vs DOSSIER

**Module**
Avantage : En créant un Module, tu rends facile l'import de nombreux composants, directives et pipes réutilisables avec une seule ligne d'importation. Cela est particulièrement utile lorsque tu veux réutiliser ces éléments à travers différents modules de ton application. Tu peux simplement importer le Module et tout ce qui est déclaré et exporté dans celui-ci sera disponible.

Scalabilité : Si ton projet devient grand et que tu as beaucoup de composants réutilisables, un module te permet de tout gérer de manière organisée. De plus, il devient facile de gérer les dépendances, d'assurer que les imports et exports sont gérés de manière centralisée.

**Dossier**
Avantage : C'est une solution simple, qui peut être suffisante si tu as peu de composants réutilisables. Tu peux simplement placer les composants dans un dossier /shared (ou /core), et les importer individuellement là où tu en as besoin

Limitation : Le principal inconvénient ici est la répétition. Si tu dois importer des composants dans de nombreux modules, tu devras les déclarer individuellement à chaque fois, ce qui peut rendre le code verbeux et potentiellement moins organisé à mesure que le projet grandit.


| /src
|__ /app
|____   /core
|________   /services
|________   /components
|________   /directives
|________   /pipes
|________   /guards
|________   /resolvers

|____   /layouts
|________   /main-layout
              - header-main
                - router-outlet 
              - footer-main
  
|________   /tenant-layout

|____   /pages
|________   /home
|____________   /components
|________________   - main-layout
|________   /new-world
|________   /throne-liberty
|________   /pricing
|________   /about
