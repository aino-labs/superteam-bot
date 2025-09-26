from django.contrib import admin
from events.models import Event
from .signals import _thread_locals


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
    def save_model(self, request, obj, form, change):
        _thread_locals.is_admin = True
        super().save_model(request, obj, form, change)
        _thread_locals.is_admin = False
