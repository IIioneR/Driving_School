from django.urls import path

from apps.driving.api.views import TicketListView

urlpatterns = [
    # /api/driving
    path(
        'tickets/',
        TicketListView.as_view(),
        name='api_driving_list')
]
