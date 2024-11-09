from django_tenants.utils import schema_context, get_tenant_model
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class TenantSchemaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Récupérer le schéma du tenant depuis les paramètres de la requête GET ou POST
        schema_name = request.GET.get('tenant') or request.POST.get('tenant')

        # Vérifier si le chemin de la request commence par /tenant
        if schema_name:
            TenantModel = get_tenant_model()
            # Récupérer le tenant associé
            tenant = get_object_or_404(TenantModel, schema_name=schema_name)

            # Utiliser le contexte du schéma tenant pour la requête
            with schema_context(schema_name):
                response = self.get_response(request)
            return response
        else:
            # Si aucun tenant n'est spécifié, utiliser le schéma public
            with schema_context("public"):
                response = self.get_response(request)
            return response