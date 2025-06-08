from django.apps import AppConfig

from django.apps import AppConfig

class PricingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pricing'

    def ready(self):
        import pricing.signals

class PricingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pricing'
