from django.db import models


class Subscribe(models.Model):
    chat_id = models.CharField(
        'Chat id',
        unique=True,
        max_length=128,
    )

    class Meta:
        db_table = 'subscribes'
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"
