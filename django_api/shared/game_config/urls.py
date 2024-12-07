from rest_framework.routers import DefaultRouter
from .views import GameViewSet, ServerViewSet, FactionViewSet

router = DefaultRouter()

router.register(r'games', GameViewSet)
router.register(r'servers', ServerViewSet)
router.register(r'factions', FactionViewSet)

urlpatterns = router.urls

