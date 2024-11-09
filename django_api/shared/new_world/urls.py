from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shared.new_world import views

router = DefaultRouter()
router.register(r'', views.NwCompanyViewSet)


urlpatterns = [
    path('', include(router.urls)),
]