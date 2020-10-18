from django.urls import path
from .views import locations
from .views import launches


urlpatterns = [
    path('top-locations/', locations.TopLocationsAPIView.as_view(), name='top-locations'),
    path('top-countries/', locations.TopCountriesAPIView.as_view(), name='top-countries'),
    path('average-cost/', launches.AverageCostAPIView.as_view(), name='average-cost'),
    path('successful-launches/', launches.SuccessfulLaunchesAPIView.as_view(), name='successful-launches'),
    path('top-month-for-launches/', launches.TopMonthForLaunchesAPIView.as_view(), name='top-month-for-launches'),
    path('locations/', locations.LocationList.as_view(), name='locations'),
    path('launches/', launches.LaunchList.as_view(), name='launches'),
]
