from rest_framework import generics, permissions

from apps.driving.api.serializers import TicketSerializer, ChapterSerializer
from apps.driving.models import Ticket, Chapter


class TicketListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class ChapterListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()

