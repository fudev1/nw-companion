from django.urls import path
from games.new_world.characters import views

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character-list'),
    path('<int:pk>/', views.CharacterDetailView.as_view(), name='character-detail')
]