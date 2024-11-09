from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tenant.discord.roles.views import DiscordRoleViewSet

router = DefaultRouter()
router.register(r'', DiscordRoleViewSet)

urlpatterns = [
    path('', include(router.urls))
]