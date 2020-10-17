from rest_framework import serializers
from rocketlaunch.models import Location, Launch


# A ModelSerializer is simply a shortcut for creating serializer
# classes with an automatic set of fields and simple default
# implementations for the create() and update() methods.
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'location']


class LaunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Launch
        fields = ['id', 'name', 'cost', 'time_date']
