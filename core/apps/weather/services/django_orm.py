from typing import Iterable

from django.db.models import Q

from core.apps.weather.entities.city import City
from core.apps.weather.exceptions.service import CityNameNotGivenException
from core.apps.weather.filters.city import CityFilters
from core.apps.weather.services.base import BaseCityService
from core.apps.weather.models import City as CityModel


class ORMCityService(BaseCityService):

    def _build_city_query(self, filters: CityFilters) -> Q:
        query = Q()
        if filters.search is not None:
            query &= Q(name__icontains=filters.search)
        if filters.name is not None:
            query &= Q(name=filters.name)
        return query

    def get_city(self, filters: CityFilters) -> City:
        query = self._build_city_query(filters)
        if not query:
            raise CityNameNotGivenException()
        try:
            city = CityModel.objects.get(query)
        except CityModel.DoesNotExist:
            return City(id=None, name=filters.name, count_requests=0)
        return city.to_entity()

    def get_city_list(self, filters: CityFilters) -> Iterable[City]:
        query = self._build_city_query(filters)
        cities = CityModel.objects.filter(query)
        return [city.to_entity() for city in cities]

    def update_count_requests(self, city: City) -> None:
        if city.id is not None:
            city_model_object = CityModel.objects.get(id=city.id)
            city_model_object.count_requests += 1
            city_model_object.save()
