from functools import lru_cache

import punq
from punq import Scope

from core.apps.weather.services.base import BaseCityService
from core.apps.weather.services.django_orm import ORMCityService
from core.project.settings.main import WEATHER_API_TOKEN

from core.weather_integration_api.services.base import WeatherService
from core.weather_integration_api.services.weather_api import WeatherApiService


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    def build_weather_service() -> WeatherService:
        return WeatherApiService(
            api_key=WEATHER_API_TOKEN
        )

    container.register(WeatherService, factory=build_weather_service, scope=Scope.singleton)

    container.register(BaseCityService, ORMCityService)

    return container
