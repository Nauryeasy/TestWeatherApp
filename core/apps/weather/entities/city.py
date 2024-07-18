from dataclasses import dataclass

from core.apps.weather.entities.base import BaseEntity


@dataclass
class City(BaseEntity):
    name: str
    count_requests: int
