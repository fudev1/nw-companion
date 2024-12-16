from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shared.users import views
from .views import discord_login, discord_login_redirect



router = DefaultRouter()
router.register(r'', views.TenantUserViewSet, basename='tenantuser')


urlpatterns = [
    # path('', include(router.urls)),
    path('discord/login', discord_login, name='discord_login'),
    path('discord/login/redirect', discord_login_redirect, name='discord_login_redirect')
] + router.urls


"""
Combinaison des endpoints REST (via `router.urls` avec des endpoints plus spécifiques)
=> /discord/callback & /discord/login
"""