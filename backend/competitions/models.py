from django.db import models


class Competition(models.Model):
    title = models.CharField(
        'Название',
        max_length=128,
    )
    prize = models.CharField(
        'Приз',
        max_length=128,
        blank=True,
        null=True,
    )
    deadline = models.DateTimeField(
        "Срок подачи заявок",
    )
    source_url = models.URLField(
        'Исходная ссылка',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Соревнование"
        verbose_name_plural = "Соревнования"
        db_table = 'competitions'
        ordering = ['deadline']
