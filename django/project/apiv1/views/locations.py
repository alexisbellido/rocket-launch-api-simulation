from rest_framework import generics
from apiv1.serializers import LocationSerializer
from rocketlaunch.models import Location


class LocationList(generics.ListCreateAPIView):
    """
    API endpoint as a generic class-based view.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
