from venv import logger

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
from events.models import Event
from api.tasks import notify_telegram_bot
import logging


@receiver(post_save, sender=Event)
def event_created(sender, instance, created, **kwargs):
    logger.info('Event fired')
    if created:
        event_data = model_to_dict(instance)
        event_data['event_date'] = event_data['event_date'].isoformat()
        notify_telegram_bot.delay(event_data)