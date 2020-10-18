from django.db.models import Avg, Sum
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from apiv1.serializers import LaunchSerializer
from rocketlaunch.models import Launch


class LaunchList(generics.ListCreateAPIView):
    """
    API endpoint as a generic class-based view.
    """
    queryset = Launch.objects.all()
    serializer_class = LaunchSerializer


class AverageCostAPIView(APIView):
    """
    Retrieves the average cost across all launches with a cost value.
    /api/v1/average-cost
    """
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        launches_with_cost = Launch.objects.filter(cost__isnull=False).count()
        aggregates = Launch.objects.filter(cost__isnull=False).aggregate(
            total_cost=Sum('cost'),
            average_cost=Avg('cost')
        )
        data = {
            "success": True,
            "total_cost": aggregates['total_cost'],
            "average_cost": aggregates['average_cost'],
            "launches_with_cost": launches_with_cost,
        }
        return Response(data)


# TODO 2. Percent of launches where mission_status is success
class SuccessfulLaunchesAPIView(APIView):
    """
    Retrieves the percentage of successful launches.
    /api/v1/successful-launches
    """
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        data = {
            "success": True,
            "percentage_success": 100,
        }
        return Response(data)


# TODO 3. The most popular month for rocket launches
class TopMonthForLaunchesAPIView(APIView):
    """
    Retrieves the most popular month for launches.
    /api/v1/top-month-for-launches
    """
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        data = {
            "success": True,
            "top_month": "tbd",
        }
        return Response(data)
