from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shared.users import views

router = DefaultRouter()
router.register(r'', views.TenantUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]