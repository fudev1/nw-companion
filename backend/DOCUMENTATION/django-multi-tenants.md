# Base de données par serveur (Multi-Tenancy)

- Réflexion sur l'isolation de données par serveur discord à l'initialisation d'une instance du bot
- L'idée est d'éviter d'avoir une seule base de données "foure-tout" avec une relation 1to1 pour lier les utilisateurs 
- Pouvoir désactiver/activer une instance 

☑️ Chaque serveur Discord qui invite le bot aurait son propre espace dans la db  
☑️ Permet de garder les données des users bien séparées  
☑️ Comment ? **`Sharder la base de données`**.  
☑️ Chaque serveur serait attribué à un schéma différent dans la base de donnée. 

=> distribuer la charge  
=> garantit une séparation des données  
=> évite la lourdeur de créer une db différente par serveur

## Mise en place

[❓] Quid de django-tenant-user, pour la gestion des users entre les tenant (à check)

Utilisation de [`django-tenants`](https://django-tenants.readthedocs.io/en/latest/examples.html) 

---
## ➡️ Installer le package
```bash
pip install django-tenants
```

## ➡️ Paramètrer django

- Ajouter `django-tenants` aux `INSTALLED_APPS` du projet  
- Utiliser une db prenant en charge les `schemas` multiple comme **`pgsql`**

## ➡️ Modifier `settings.py`
- Définir un modèle de client tenant

```python
TENANT_MODEL = "your_app.Client"
```
- Définir le `schema` par défaut pour la db

```python
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        #'NAME': 'your_database_name',
        #'USER': 'your_database_user',
        #'PASSWORD': 'your_password',
        #'HOST': 'localhost',
        #'PORT': '5432',
    }
}
```

## ➡️ Créer un modèle `Client` ou `Tenant`, ...
- Chaque `tenant` est représenté par une instance de ce modèle
- `TenantMixin` : utilisé pour créer les tenants (chaque serveur discord)

```python
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class DiscordClient(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    created_on = models.DateField(auto_now_add=True)

    # defaut à True => le schema sera automatiquement créé et synchro 
    auto_create_schema = True

class Domain(DomainMixin):
    pass
```

## ➡️ Faire les migrations pour les tenants
- Pour chaque nouveau tenant, il faudra `créer un schema PostgreSQL`
- Appliquer les migrations communes (models partagés entre tous les tenants)
```bash
python manage.py migrate_schemas --shared
```

## ➡️ Domaine pour les tenants
- Dans django-tenants, un `domaine` est lié à un `tenant`
- Utilisé pour identifier des tenants via des sous domaines ou des url différentes

```python
domain = Domain()
domain.domain = 'example.com'
domain.tenant = client_instance
domain.is_primary = True
domain.save()
```

## ➡️ Routage des request en fonction des `tenants`
- `django-tenants`gère seul le routage des request entrantes vers le tenant correspondant
- Basé sur le `domaine`
- => configurer le `middleware`pour le package qui interceptera chaque request pour la diriger vers le schéma approprié.

```python
MIDDLEWARE = [
    'django_tenants.middleware.TenantMiddleware',
    ...
]
```
## ➡️ Séparer les `Données` et `Modèles` spécifiques
- Certains modèles seront communs à tous les tenants (ex: User, ..)
- D'autres seront spécifiques à chaque tenant (Member)

## ➡️ Fixture et tests
- **`Fixtures`** : Pour chaque tenant, si on souhaite charger des fixtures, il faudra le faire en spécifiant explicitement le tenant.
- **`Tests Unitaire`* : Créer des tests qui couvrent les interactions multi-tenants. 

## ➡️ Gestion des Permissions et des Accès
- Chaque tenant représente un `client` différent (serveur Discord), s'assurer qur la gestion des permission est OK
- Le bot doit uniquement avoir accès aux données spécifiques au tenant auquel il est associé. 
- => Ajouter un filtrage dans les request basées sur les tenants





