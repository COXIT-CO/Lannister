from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Bonus_request, Bonus_request_history


@receiver(post_save, sender=Bonus_request)
def post_save_create_Bonus_request_history(sender, instance, created, **kwargs):
    if created:
        Bonus_request_history.objects.create(request_id=instance)
