from rest_framework import serializers

from apps.driving.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'chapter', 'question', 'answer', 'explanation']
        read_only_fields = ['id', 'explanation']
