from abc import ABC, abstractmethod

from core.apps.weather.entities.city import City
from core.apps.weather.filters.city import CityFilters


class BaseCityService(ABC):

    @abstractmethod
    def get_city(self, filters: CityFilters) -> City:
        ...

    @abstractmethod
    def get_city_list(self, filters: CityFilters) -> list[City]:
        ...

    @abstractmethod
    def update_count_requests(self, city: City) -> None:
        ...
