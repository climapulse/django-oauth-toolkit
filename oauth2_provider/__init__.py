import django


__version__ = "2.3.1"

if django.VERSION < (3, 2):
    default_app_config = "oauth2_provider.apps.DOTConfig"
