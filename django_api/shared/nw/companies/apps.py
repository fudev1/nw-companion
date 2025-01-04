from django.apps import AppConfig


class NewWorldConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shared.nw.companies'
    label = 'nw_public_companies'
