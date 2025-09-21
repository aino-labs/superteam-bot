from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'event_date',
            'location',
            'source_url',
        )

        extra_kwargs = {
            'location': {'required': False},
            'source_url': {'required': False},
        }

        read_only_fields = ('id', )
