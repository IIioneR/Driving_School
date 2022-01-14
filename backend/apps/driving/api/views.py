from rest_framework import generics, permissions

from apps.driving.api.serializers import TicketSerializer
from apps.driving.models import Ticket


class TicketListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
