from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'character', views.CharacterViewSet)
router.register(r'role', views.RoleViewSet)
router.register(r'profile', views.MemberProfileViewSet)
router.register(r'character_role', views.CharacterRoleViewSet)

urlpatterns = [
    path('', include(router.urls))
]