from django.urls import path
from .views import locations
from .views import launches


urlpatterns = [
    path('locations/', locations.LocationList.as_view()),
    path('launches/', launches.LaunchList.as_view()),
]
