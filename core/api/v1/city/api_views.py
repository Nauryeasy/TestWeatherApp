import punq
from django.http import HttpRequest, JsonResponse
from rest_framework.views import APIView

from core.api.v1.city.serializers import CitySerializer, ForecastSerializer
from core.apps.weather.exceptions.service import CityNameNotGivenException

from core.apps.weather.filters.city import CityFilters
from core.apps.weather.services.base import BaseCityService
from core.project.container import get_container
from core.weather_integration_api.exceptions.weather_api_services import LocationNotFoundException
from core.weather_integration_api.services.base import WeatherService


class GetCitiesListApiView(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        container: punq.Container = get_container()
        city_service: BaseCityService = container.resolve(BaseCityService)
        city_name = request.GET.get('city', None)
        filters = CityFilters(
            search=city_name
        )

        cities = city_service.get_city_list(filters)
        return JsonResponse(CitySerializer(cities, many=True).data, safe=False)


class GetWeatherForecastApiView(APIView):
    def get(self, request: HttpRequest) -> JsonResponse:
        container: punq.Container = get_container()
        city_service: BaseCityService = container.resolve(BaseCityService)
        weather_service: WeatherService = container.resolve(WeatherService)

        city_name = request.GET.get('city', None)
        filters = CityFilters(
            name=city_name
        )

        try:
            city = city_service.get_city(filters)
        except CityNameNotGivenException as e:
            return JsonResponse({'error': e.__class__.__name__, 'message': e.message}, status=400)

        try:
            forecast = weather_service.get_weather(city.name)
        except LocationNotFoundException as e:
            return JsonResponse({'error': e.__class__.__name__, 'message': e.message}, status=400)

        city_service.update_count_requests(city)

        return JsonResponse(ForecastSerializer(forecast).data, safe=False)
