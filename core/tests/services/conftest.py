import pytest

from core.apps.weather.services.base import BaseCityService
from core.apps.weather.services.django_orm import ORMCityService


@pytest.fixture
def city_service() -> BaseCityService:
    return ORMCityService()
