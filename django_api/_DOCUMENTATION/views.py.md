## Tout le monde voit tout : 

```py
class NwCharacterViewSet(viewsets.ModelViewSet):
    queryset = NwCharacter.objects.all()  # Définition statique
    serializer_class = NwCharacterSerializer
```
=> Résultat : N'importe qui peut voir tous les perso

## Restriction par authentification et queryset :

```py
class NwCharacterViewSet(viewsets.ModelViewSet):
    # Pas de queryset défini ici
    serializer_class = NwCharacterSerializer
    permission_classes = [permissions.IsAuthenticated]  # Doit être connecté

    def get_queryset(self):
        # Cette méthode est appelée pour CHAQUE requête
        if self.request.user.is_staff:
            return NwCharacter.objects.all()  # Admin voit tout
        return NwCharacter.objects.filter(user=self.request.user)  # Utilisateur ne voit que ses persos
```
=> Résultat : 
- Doit être connecté poru accéder (permission_classes)
- Si admin : voit tous les personnages
- Si utilisateur normal : ne voit que ses personnages

La méthode `get_queryset` est appélée à chaque requête, ce qui permet de filtrer dynamiquement les données en fonction de l'utilisateur qui fait la requête. 


## besoins spécifiques : 
```py
class NwCharacterViewSet(viewsets.ModelViewSet):
    queryset = NwCharacter.objects.all()  # Tout le monde peut VOIR
    serializer_class = NwCharacterSerializer

    def get_permissions(self):
        # GET = tout le monde
        # POST/PUT/DELETE = seulement si connecté
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
```