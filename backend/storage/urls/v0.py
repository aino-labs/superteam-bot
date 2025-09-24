from django.urls import include, path


urlpatterns = [
    path('competitions/', include('competitions.urls')),
    path('events/', include('events.urls')),
    path('subscribes/', include('subscribes.urls')),
]
