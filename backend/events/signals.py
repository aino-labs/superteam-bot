from venv import logger
from threading import local

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
from events.models import Event
from api.tasks import send_event_webhook
import logging

_thread_locals = local()

def is_admin_request():
    return getattr(_thread_locals, 'is_admin', False)

@receiver(post_save, sender=Event)
def event_created(sender, instance, created, **kwargs):
    logger.info('Event fired')
    if created and is_admin_request():
        event_data = model_to_dict(instance)
        event_data['event_date'] = event_data['event_date'].isoformat()
        send_event_webhook.delay([event_data])