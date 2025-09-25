
from django.db import models

class Event(models.Model):
    api_id = models.CharField(
        'API ID',
        max_length=64,
        unique=True,
        null=True,
        blank=True,
    )
    title = models.CharField(
        'Title',
        max_length=128,
    )
    event_date = models.DateTimeField(
        'Event date'
    )
    location = models.CharField(
        'Location',
        max_length=128,
        blank=True,
        null=True,
    )
    rsvp_link = models.URLField(
        'RSVP link',
        blank=True,
        null=True,
    )
    source_url = models.URLField(
        'Source URL',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        db_table = 'events'
