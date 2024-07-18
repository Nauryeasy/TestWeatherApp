from dataclasses import dataclass

from core.weather_integration_api.exceptions.base import BaseWeatherException


@dataclass(eq=False)
class LocationNotFoundException(BaseWeatherException):
    city: str

    @property
    def message(self) -> str:
        return f'Location {self.city} not found'
