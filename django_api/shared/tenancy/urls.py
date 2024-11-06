from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shared.tenancy import views


# Router pour les tenants (compagnies)
tenants_router = DefaultRouter()
tenants_router.register(r'', views.CompanyViewSet)

# Router pour les domaines
domains_router = DefaultRouter()
domains_router.register(r'', views.DomainViewSet)

urlpatterns = [
    path('tenants/', include(tenants_router.urls)),
    path('domains/', include(domains_router.urls)),
]