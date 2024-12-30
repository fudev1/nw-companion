import time 
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils.text import slugify
from django_tenants.utils import schema_context, get_public_schema_name, get_tenant_domain_model, has_multi_type_tenants, get_tenant_types, get_multi_type_database_field_name
from tenant_users.tenants.models import ExistsError, InactiveError, SchemaError
from shared.new_world.companies.models import NwCompany
from django.core.management import call_command


@transaction.atomic()
def provision_newworld(
    tenant_name,
    tenant_slug,
    user,
    *,
    is_staff: bool = False,
    is_superuser: bool = True,
    tenant_type=None,
    schema_name=None,
    tenant_extra_data=None,
):
    
    tenant = None

    if tenant_extra_data is None: 
        tenant_extra_data = {}

    UserModel = get_user_model()
    TenantModel = NwCompany
    user = UserModel.objects.get(email=user)
    if not user.is_active:
        raise InactiveError("inactive user passed to provision tenant")
    
    if hasattr(settings, "TENANT_SUBFOLDER_PREFIX"):
        tenant_domain = tenant_slug
    else:
        tenant_domain = f"{tenant_slug}.{settings.TENANT_USERS_DOMAIN}"

    DomainModel = get_tenant_domain_model()
    if DomainModel.objects.filter(domain=tenant_domain).exists():
        raise ExistsError("Teant URL already exists")
    
    if not schema_name: 
        time_string = str(int(time.time()))
        schema_name = f"{tenant_slug}-{time_string}"

    if has_multi_type_tenants():
        valid_tenant_types = get_tenant_types()
        if tenant_type not in valid_tenant_types:
            valid_type_str = ", ".join(valid_tenant_types)
            error_message = "{} is not a valid tenant type. Choices are {}.".format(tenant_type, valid_type_str)
            raise SchemaError(error_message)
        
        tenant_extra_data.update({get_multi_type_database_field_name(): tenant_type})

    with schema_context(get_public_schema_name()):
        tenant = TenantModel.objects.create(
            slug=slugify(tenant_slug),
            name=tenant_name,
            owner=user,
            schema_name=schema_name,
            **tenant_extra_data,
        )

        domain_model = get_tenant_domain_model()
        domain_model.objects.create(
            domain=tenant_domain, tenant=tenant, is_primary=True
        )

        tenant.add_user(user, is_superuser=is_superuser, is_staff=is_staff)
    
        run_migrations_for_tenant(tenant)

    return tenant_domain


def run_migrations_for_tenant(tenant):
    with schema_context(tenant.schema_name):
        call_command('migrate', '--noinput')