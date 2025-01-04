from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import NwBuildViewSet

router = DefaultRouter()
router.register(r'', NwBuildViewSet)

urlpatterns = [
    path('', include(router.urls))
]




