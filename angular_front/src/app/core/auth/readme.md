1. Utiliser un service d'authentification central qui gèrera :
-> L'état de l'utilisateur (isLoggedIn, userInfo, etc.)
-> La logique de connexion et de déconnexion

Ce service peut utiliser (l'un ou l'autre) 
-> les signaux (Angular Signals) 
-> BehaviorSubject de RxJS 
pour émettre des événements lorsque l'utilisateur se connecte ou se déconnecte.

2. Créer un composant Profil réutilisable pour le Bouton Profil
-> /core/layout/header/auth-button/
-> Affichera soit le bouton de connexion soit le profil de l'utilisateur

3. Inclure le composant dans le Header
-> Ajouter dans chaque header de manière conditionnelle

4. Utiliser ngIf pour afficher ou non le composant

- auth.service.ts suivra si l'utilisateur est connecté ou non
- utiliser le localStorage pour mémoriser le token ou l'état de connexion
- si l'user clique sur "se connecter", initier le process OAuth