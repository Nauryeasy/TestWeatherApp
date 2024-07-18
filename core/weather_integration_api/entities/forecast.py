from dataclasses import dataclass

from core.weather_integration_api.entities.base import BaseWeatherEntity


@dataclass(frozen=True)
class ForecastEntity(BaseWeatherEntity):
    city_name: str
    max_temp: float
    min_temp: float
    avg_temp: float
    max_wind_speed: float
    total_precip: float
    total_snow: float
    avg_visibility: float
    avg_humidity: int
    weather_condition: str
    daily_will_it_rain: bool
    daily_will_it_snow: bool
    daily_chance_of_rain: int
    daily_chance_of_snow: int
