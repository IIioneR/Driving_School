from django.urls import path, include

urlpatterns = [
    # /api/...
    path('driving/', include('apps.driving.api.urls'))
]
