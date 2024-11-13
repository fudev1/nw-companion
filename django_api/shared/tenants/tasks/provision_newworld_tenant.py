# import logging
# from django.conf import settings
# from django_tenants.utils import get_public_schema_name, get_tenant_domain_model, get_tenant_model, schema_context

# from tenant_users.tenants.tasks import provision_tenant
# from shared.new_world.models import NwCompany
# from django.db import transaction
# from django.contrib.auth import get_user_model
# from django_tenants.utils import tenant_context


# @transaction.atomic
# def provision_newworld_tenant(user, nwcompany_data):
#     tenant_name = nwcompany_data['name']
#     tenant_slug = tenant_name.lower().replace(' ', '_')
#     tenant_domain = f"{tenant_slug}.{settings.TENANT_USERS_DOMAIN}"

#     try:
#         tenant, domain = provision_tenant(
#             tenant_name=tenant_name,
#             tenant_slug=tenant_slug,
#             owner=user,
#             is_superuser=True,
#             is_staff=True,
#         )
#         print(f"provision tenant result: {tenant}, {domain}")

#         nwcompany = NwCompany.objects.create(
#             name=tenant_name,
#             schema_name=tenant_slug,
#             owner=user,
#             email=user.email,
#             server=nwcompany_data['server'],
#             faction=nwcompany_data['faction']
#         )

#         transaction.set_rollback(True)

#     except Exception as e:
#         raise e
    
#     return tenant_slug, domain.domain, nwcompany

# def get_tenant_context(nwcompany_id):
#     nwcompany = NwCompany.objects.get(id=nwcompany_id)
#     return tenant_context(nwcompany)