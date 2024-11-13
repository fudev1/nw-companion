import time
from typing import Optional, Tuple
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django_tenants.utils import (
    get_multi_type_database_field_name,
    get_public_schema_name,
    get_tenant_domain_model,
    get_tenant_types,
    has_multi_type_tenants,
    schema_context,
)

from tenant_users.tenants.models import ExistsError, InactiveError, SchemaError
from shared.new_world.models import NwCompany


UserModel = get_user_model()
DomainModel = get_tenant_domain_model()


MODEL_MAPPING = {
    "new_world": {
        "model": NwCompany,
        "abbreviation": "nw",
    },
}


@transaction.atomic()
def provision_tenant(
    tenant_name: str,
    tenant_slug: str,
    owner: UserModel,
    *,
    is_staff: bool = False,
    is_superuser: bool = True,
    tenant_type: Optional[str] = None,
    schema_name: Optional[str] = None,
    tenant_extra_data: Optional[dict] = None,
) -> Tuple[object, DomainModel]:
    
    """Crée et initialise un nouveau tenant avec les attributs spécifiés et les rôles par défaut."""


    if tenant_extra_data is None:
        tenant_extra_data = {}

    if not owner.is_active:
        raise InactiveError("L'utilisateur fourni est inactif.")

    if tenant_type not in MODEL_MAPPING:
        raise ValueError(f"Type de tenant non supporté: {tenant_type}")

    TenantModel = MODEL_MAPPING[tenant_type]['model']

    if hasattr(settings, "TENANT_SUBFOLDER_PREFIX"):
        tenant_domain = tenant_slug
    else:
        tenant_domain = f"{tenant_slug}.{settings.TENANT_USERS_DOMAIN}"

    if DomainModel.objects.filter(domain=tenant_domain).exists():
        raise ExistsError("L'URL du tenant existe déjà.")

    if not schema_name:
        # time_string = str(int(time.time()))
        server = tenant_extra_data['server'].lower()
        game_type = MODEL_MAPPING[tenant_type]["abbreviation"]

        schema_name = f"{tenant_slug}_{server}_{game_type}"

    if has_multi_type_tenants():
        valid_tenant_types = get_tenant_types()

        if tenant_type not in valid_tenant_types:
            valid_type_str = ", ".join(valid_tenant_types)
            error_message = f"{tenant_type} n'est pas un type de tenant valide. Choix possibles: {valid_type_str}."
            raise SchemaError(error_message)

        tenant_extra_data.update({get_multi_type_database_field_name(): tenant_type})
    
    # Créer le tenant dans le contexte du schéma public
    with schema_context(get_public_schema_name()):
        tenant = TenantModel.objects.create(
            name=tenant_name,
            slug=tenant_slug,
            schema_name=schema_name,
            owner=owner,
            **tenant_extra_data,
        )

        # Créer un domaine associé au tenant et le marquer comme primaire
        domain = DomainModel.objects.create(
            domain=tenant_domain, tenant=tenant, is_primary=True
        )

        # Ajouter l'utilisateur au tenant avec les rôles spécifiés
        tenant.add_user(owner, is_superuser=is_superuser, is_staff=is_staff)

    # Retourner le tenant et son domaine associé
    return tenant, domain