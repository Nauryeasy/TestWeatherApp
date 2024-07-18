import pytest

from core.apps.weather.exceptions.service import CityNameNotGivenException
from core.apps.weather.filters.city import CityFilters
from core.apps.weather.services.base import BaseCityService


@pytest.mark.django_db
def test_get_city(city_service: BaseCityService):
    filters = CityFilters(
        name='Москва'
    )

    city = city_service.get_city(filters)
    assert city.name == 'Москва'


def test_get_city_raises_exception(city_service: BaseCityService):
    filters = CityFilters(
        name=None
    )

    with pytest.raises(CityNameNotGivenException):
        city_service.get_city(filters)
