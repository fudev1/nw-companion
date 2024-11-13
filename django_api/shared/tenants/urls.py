from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shared.tenants import views
# from shared.tenants.views import ProvisionCompany


# Router pour les tenants (compagnies)
# tenants_router = DefaultRouter()
# tenants_router.register(r'', views.TenantViewSet)

# # Router pour les domaines
# domains_router = DefaultRouter()
# domains_router.register(r'', views.DomainViewSet)

# urlpatterns = [
#     path('tenants/', include(tenants_router.urls)),
#     path('domains/', include(domains_router.urls)),
# ]


router = DefaultRouter()
router.register(r'', views.TenantViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('provision_nwcompany/', ProvisionCompany.as_view(), name='provision_nwcompany'),
]