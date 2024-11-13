from django.urls import path, include

urlpatterns = [
    path('character/', include('games.new_world.characters.urls')),
    # path('wars/', include('games.new_world.wars.urls')),
    # ...
]