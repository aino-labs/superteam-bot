from rest_framework import serializers

from competitions.models import Competition


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = (
            'id',
            'title',
            'prize',
            'deadline',
            'source_url',
        )

        extra_kwargs = {
            'prize': {'required': False},
            'source_url': {'required': False},
        }

        read_only_fields = ('id', )
