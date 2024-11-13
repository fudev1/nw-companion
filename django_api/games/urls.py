from django.urls import path, include

urlpatterns = [
    path('new_world/', include('games.new_world.urls')),
    # path('other_game/', include('games.other_game.urls')),
    # ...
]