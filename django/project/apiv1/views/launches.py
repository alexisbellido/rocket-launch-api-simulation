from rest_framework import generics
from apiv1.serializers import LaunchSerializer
from rocketlaunch.models import Launch


class LaunchList(generics.ListCreateAPIView):
    """
    API endpoint as a generic class-based view.
    """
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer

# TODO
# 1. Average launch cost (excluding nulls)

# 2. Percent of launches where mission_status is success

# 3. The most popular month for rocket launches