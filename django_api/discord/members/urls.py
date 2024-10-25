from django.urls import path, include
from rest_framework.routers import DefaultRouter
from discord.members.views import MemberProfileViewSet

router = DefaultRouter()
router.register(r'', MemberProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]