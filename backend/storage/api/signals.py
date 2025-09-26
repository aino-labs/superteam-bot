from celery.signals import worker_ready
from .tasks import fetch_events, fetch_challenges


@worker_ready.connect
def at_start(sender, **kwargs):
    fetch_events.delay()
    fetch_challenges.delay()
