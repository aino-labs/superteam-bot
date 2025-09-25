from celery.signals import worker_process_init
from .tasks import fetch_events, fetch_challenges

@worker_process_init.connect
def at_start(sender, **kwargs):
    fetch_events.delay()
    fetch_challenges.delay()
