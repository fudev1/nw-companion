from django.urls import path, include
from rest_framework.routers import DefaultRouter
from discord.roles.views import DiscordRoleViewSet

router = DefaultRouter()
router.register(r'', DiscordRoleViewSet)

urlpatterns = [
    path('', include(router.urls))
]