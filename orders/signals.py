from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Order


@receiver(post_save, sender=Order)
def update_on_save(sender, instance, created, **kwargs):
    """
    Updates order total update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=Order)
def update_on_delete(sender, instance, **kwargs):
    """
    Updates order total delete
    """
    instance.order.update_total()
