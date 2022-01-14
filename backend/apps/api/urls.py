from django.urls import include, path

urlpatterns = [
    # /api/...
    path('driving/', include('apps.driving.api.urls'))
]
