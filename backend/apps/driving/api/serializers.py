from rest_framework import serializers

from apps.driving.models import Ticket, Chapter


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'chapter', 'question', 'answer', 'explanation']
        read_only_fields = ['id', 'explanation']


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'text']
        read_only_fields = ['id', 'text']
