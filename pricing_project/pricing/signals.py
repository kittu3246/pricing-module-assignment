from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PricingConfig, PricingLog
from threading import local

_user = local()

def set_actor(user):
    _user.value = user

def get_actor():
    return getattr(_user, 'value', None)

@receiver(post_save, sender=PricingConfig)
def log_pricing_config_save(sender, instance, created, **kwargs):
    actor = get_actor()
    action = "created" if created else "updated"
    PricingLog.objects.create(
        pricing_config=instance,
        action=action,
        actor=actor,
        description=f"Pricing config {action}.",
    )

@receiver(post_delete, sender=PricingConfig)
def log_pricing_config_delete(sender, instance, **kwargs):
    actor = get_actor()
    PricingLog.objects.create(
        pricing_config=instance,
        action="deleted",
        actor=actor,
        description="Pricing config deleted."
    )
