from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import NwRegionViewSet, NwServerViewSet

router = DefaultRouter()
router.register(r'regions', NwRegionViewSet, basename='nwregion')
router.register(r'servers', NwServerViewSet, basename='nwserver')

urlpatterns = [
    path('', include(router.urls)),
]
