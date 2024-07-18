from dataclasses import dataclass


@dataclass(eq=False)
class CityNameNotGivenException(Exception):
    @property
    def message(self) -> str:
        return 'City name is not given'
