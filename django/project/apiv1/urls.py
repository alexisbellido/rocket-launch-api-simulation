from django.urls import path
from .views import locations
from .views import launches


urlpatterns = [
    path('locations/', locations.LocationList.as_view(), name='locations'),
    path('top-locations/', locations.TopLocationsAPIView.as_view(), name='top-locations'),
    path('launches/', launches.LaunchList.as_view(), name='launches'),
]
