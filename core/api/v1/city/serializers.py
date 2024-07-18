from rest_framework import serializers


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    count_requests = serializers.IntegerField()


class ForecastSerializer(serializers.Serializer):
    city_name = serializers.CharField(max_length=255)
    max_temp = serializers.FloatField()
    min_temp = serializers.FloatField()
    avg_temp = serializers.FloatField()
    max_wind_speed = serializers.FloatField()
    total_precip = serializers.FloatField()
    total_snow = serializers.FloatField()
    avg_visibility = serializers.FloatField()
    avg_humidity = serializers.IntegerField()
    weather_condition = serializers.CharField(max_length=255)
    daily_will_it_rain = serializers.BooleanField()
    daily_will_it_snow = serializers.BooleanField()
    daily_chance_of_rain = serializers.IntegerField()
    daily_chance_of_snow = serializers.IntegerField()
