from django.contrib import admin
from competitions.models import Competition


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'prize',
        'deadline',
        'source_url',
    )
