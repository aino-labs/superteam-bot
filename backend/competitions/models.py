from django.db import models


class Competition(models.Model):
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
    prize = models.CharField(
        'Prize',
        max_length=128,
        blank=True,
        null=True,
    )
    deadline = models.DateTimeField(
        "Application deadline",
    )
    source_url = models.URLField(
        'Source URL',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Competition"
        verbose_name_plural = "Competitions"
        db_table = 'competitions'
        ordering = ['deadline']
