from abc import ABC, abstractmethod

from core.weather_integration_api.entities.forecast import ForecastEntity


class WeatherService(ABC):
    @abstractmethod
    def get_weather(self, city: str) -> ForecastEntity:
        ...
