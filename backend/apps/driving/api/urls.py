from django.urls import path

from apps.driving.api.views import TicketExaminationListView

urlpatterns = [
    # /api/driving
    path(
        'tickets/',
        TicketExaminationListView.as_view(),
        name='api_driving_list')
]
