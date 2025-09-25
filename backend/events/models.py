
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
        'Название',
        max_length=128,
    )
    event_date = models.DateTimeField(
        'Дата проведения'
    )
    location = models.CharField(
        'Место проведения',
        max_length=128,
        blank=True,
        null=True,
    )
    rsvp_link = models.URLField(
        'Ссылка RSVP',
        blank=True,
        null=True,
    )
    source_url = models.URLField(
        'Исходная ссылка',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        db_table = 'events'
