from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NwCharacterViewSet

router = DefaultRouter()
router.register(r'new-world', NwCharacterViewSet, basename='nw-character')

urlpatterns = [
    path('', include(router.urls)),
]