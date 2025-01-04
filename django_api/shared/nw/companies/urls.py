from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shared.new_world.companies import views

router = DefaultRouter()
router.register(r'companies', views.NwCompanyViewSet, basename='nwcompany')


urlpatterns = [
    path('', include(router.urls)),
]