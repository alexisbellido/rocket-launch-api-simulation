from datetime import datetime
from django.db.models import Avg, Sum, Count
from django.db.models.functions import ExtractMonth
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from apiv1.serializers import LaunchSerializer
from rocketlaunch.models import Launch, Status


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


class SuccessfulLaunchesAPIView(APIView):
    """
    Retrieves the percentage of successful launches.
    /api/v1/successful-launches
    """
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        total_launches = Launch.objects.all().count()
        successful_launches = Launch.objects.filter(status__id=Status.SUCCESS).count()
        percentage_success = round((successful_launches * 100) / total_launches, 2)
        data = {
            "success": True,
            "total_launches": total_launches,
            "successful_launches": successful_launches,
            "percentage_success": percentage_success,
        }
        return Response(data)


class TopMonthForLaunchesAPIView(APIView):
    """
    Retrieves the most popular month for launches.
    /api/v1/top-month-for-launches
    """
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        month_counter = Launch.objects.annotate(
            month=ExtractMonth('time_date')
            ).values('month').annotate(count=Count('id')).order_by('-month')[0]
        data = {
            "success": True,
            "top_month": month_counter['month'],
            "top_month_name": datetime.strptime(str(month_counter['month']), "%m").strftime('%B'),
            "launches_count": month_counter['count']
        }
        return Response(data)
