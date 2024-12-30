1. redirection login

2. redirection callback 
    => recevoir code autorisation temporaire 
    => échanger contre access token

3. créer l'utilisateur 
    => vérifier si existe 
    > oui : mettre à jour les infos
    > non : ajouter l'user


1. L'utilisateur clique sur "Login with Discord"
2. Il est redirigé vers Discord pour autorisation
3. Discord renvoie un code à votre backend
4. coté backend :
- Échange le code contre un token Discord
- Récupère les infos utilisateur de Discord
- Crée/met à jour l'utilisateur dans votre DB
- Génère un JWT avec RefreshToken.for_user(user)
- Redirige vers le frontend avec le token