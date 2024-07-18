"""
https://www.weatherapi.com/docs/
"""
import requests

from core.weather_integration_api.entities.forecast import ForecastEntity
from core.weather_integration_api.exceptions.weather_api_services import LocationNotFoundException
from core.weather_integration_api.services.base import WeatherService


class WeatherApiService(WeatherService):

    api_forecast_url: str = 'http://api.weatherapi.com/v1/forecast.json'

    def __init__(self, api_key: str):
        self.api_key: str = api_key

    def get_weather(self, city: str) -> ForecastEntity:

        params = {
            'key': self.api_key,
            'q': city,
            'lang': 'ru',
        }

        forecast_api_result = requests.get(self.api_forecast_url, params=params).json()
        if 'error' in forecast_api_result:
            if forecast_api_result['error']['code'] == 1006:
                raise LocationNotFoundException(city=city)

        forecast_day = forecast_api_result['forecast']['forecastday'][0]['day']

        return ForecastEntity(
            city_name=forecast_api_result['location']['name'],
            max_temp=forecast_day['maxtemp_c'],
            min_temp=forecast_day['mintemp_c'],
            avg_temp=forecast_day['avgtemp_c'],
            max_wind_speed=forecast_day['maxwind_kph'],
            total_precip=forecast_day['totalprecip_mm'],
            total_snow=forecast_day['totalsnow_cm'],
            avg_visibility=forecast_day['avgvis_km'],
            avg_humidity=forecast_day['avghumidity'],
            weather_condition=forecast_day['condition']['text'],
            daily_will_it_rain=bool(forecast_day['daily_will_it_rain']),
            daily_will_it_snow=bool(forecast_day['daily_will_it_snow']),
            daily_chance_of_rain=forecast_day['daily_chance_of_rain'],
            daily_chance_of_snow=forecast_day['daily_chance_of_snow'],
        )


if __name__ == '__main__':

    service = WeatherApiService(api_key='cb098e0820594bb5aa0143919241807')
    print(service.get_weather(city='Ижевск'))
