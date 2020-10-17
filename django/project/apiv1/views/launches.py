from rest_framework import generics
from apiv1.serializers import LaunchSerializer
from rocketlaunch.models import Launch


class LaunchList(generics.ListCreateAPIView):
    """
    API endpoint as a generic class-based view.
    """
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer
