core/
├── settings.py
├── urls.py
games/                              # Module qui reprends les besoins pour chaque tenants
├── discord/                        # Module pour la gestion discord
│   ├── members/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── roles/                      # Module pour la gestion des roles discord
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
├── new_world/                      # Module pour le jeu New World
│   ├── characters/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   └── wars/                       # Module pour la gestion des guerres
|       ├── models.py
|       ├── serializers.py
|       ├── views.py
|       └── urls.py
shared/                             # Module pour tous les modules communs aux tenants
├── game_config/                    # Module pour le config des jeux
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── new_world/                      # Module pour le jeu New World
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── tenants/                        # Module pour la gestion des tenants
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── users/                          # Module pour la gestion des utilisateurs  
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py





