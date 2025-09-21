from django.contrib import admin
from events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'event_date',
        'location',
        'rsvp_link',
        'source_url',
    )
