from tenant_users.tenants.tasks import provision_tenant
from django.core.management import call_command
from django.db import transaction
from shared.tenants.models import Tenant
from shared.new_world.companies.models import NwCompany

@transaction.atomic
def provision_nwcompany(tenant_name, tenant_slug, user, server, faction, **kwargs):
    # Créer le tenant
    tenant, domain = provision_tenant(
        tenant_name=tenant_name,
        tenant_slug=tenant_slug,
        owner=user,
        **kwargs
    )

    # Exécuter les migrations pour le schéma tenant
    call_command('migrate_schemas', schema_name=tenant.schema_name, noinput=True)

    # Créer les données spécifiques au jeu New World
    nw_company = NwCompany.objects.create(
        tenant_ptr=tenant,
        server=server,
        faction=faction,
    )

    return tenant, domain, nw_company