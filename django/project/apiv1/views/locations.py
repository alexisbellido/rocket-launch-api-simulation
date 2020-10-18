from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from apiv1.serializers import LocationSerializer
from rocketlaunch.models import Location, Launch


class LocationList(generics.ListCreateAPIView):
    """
    API endpoint as a generic class-based view.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# TODO group by location and count
class TopLocationsAPIView(APIView):
    """
    Retrieves the top launch locations.
    The default is three locations and you can pass
    a different number using the limit query parameter.
 
    /api/v1/top-locations/?limit=5
    """
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        limit = request.query_params.get("limit", 3)

        data = {
            "success": True,
            "limit": int(limit),
        }
        return Response(data)

# 2. Top three countries where launch_locations take place
# accept query parameter that defaults to 3
