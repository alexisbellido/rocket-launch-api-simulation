from django.db.models import Count
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


class TopLocationsAPIView(APIView):
    """
    Retrieves the top launch locations.
    The default is three locations and you can pass
    a different number using the limit query parameter.
 
    /api/v1/top-locations/?limit=5
    """
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        top_locations = []
        limit = int(request.query_params.get("limit", 3))
        locations_counter = Location.objects.annotate(count_launches=Count('launch__id')).order_by('-count_launches')[:limit]
        for location in locations_counter:
            top_locations.append({
                "id": location.id,
                "location": location.location,
                "count_launches": location.count_launches,
            })
        data = {
            "success": True,
            "top_locations": top_locations,
            "limit": int(limit),
        }
        return Response(data)


# TODO
# 2. Top three countries where launches take place
class TopCountriesAPIView(APIView):
    """
    Retrieves the top countries where launches take place.
    The default is three countries and you can pass
    a different number using the limit query parameter.
 
    /api/v1/top-countries/?limit=5
    """
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        top_countries = []
        limit = int(request.query_params.get("limit", 3))
        data = {
            "success": True,
            "top_countries": top_countries,
            "limit": int(limit),
        }
        return Response(data)
