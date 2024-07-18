from dataclasses import dataclass


@dataclass(eq=False)
class BaseWeatherException(Exception):

    @property
    def message(self) -> str:
        return 'An error occurred while receiving the weather forecast'

    def __str__(self) -> str:
        return self.message
