from django.urls import path

from apps.driving.api.views import TicketListView, ChapterListView

urlpatterns = [
    # /api/driving
    path(
        'tickets/',
        TicketListView.as_view(),
        name='api_tickets_list'),
    path(
        'chapters/',
        ChapterListView.as_view(),
        name='api_chapters_list')
]
