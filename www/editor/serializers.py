from rest_framework.serializers import ModelSerializer

from editor import models


class RouteSerializer(ModelSerializer):
    class Meta:
        model = models.Route
        fields = ['id','name', 'description', 'platforms']


class PlatformTypeSerializer(ModelSerializer):
    class Meta:
        model = models.PlatformType
        fields = ['id','name', 'description']


class RoutePlatformSerializer(ModelSerializer):
    class Meta:
        model = models.RoutePlatform
        fields = ['prev', 'next', 'name', 'type', 'route', 'longitude', 'latitude', 'description']


class RoutePointSerializer(ModelSerializer):
    class Meta:
        model = models.RoutePoint
        fields = ['prev', 'next', 'route', 'longitude', 'latitude', 'description']

