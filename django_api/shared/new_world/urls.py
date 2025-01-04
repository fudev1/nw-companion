from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import NwRegionViewSet, NwServerViewSet, NwFactionViewSet, NwRoleViewSet

router = DefaultRouter()
router.register(r'regions', NwRegionViewSet, basename='nwregion')
router.register(r'servers', NwServerViewSet, basename='nwserver')
router.register(r'factions', NwFactionViewSet, basename='nwfaction')
router.register(r'roles', NwRoleViewSet, basename='nwrole')

urlpatterns = [
    path('', include(router.urls)),
]
