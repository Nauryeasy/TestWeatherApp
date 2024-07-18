from dataclasses import dataclass


@dataclass(eq=False)
class BaseAppException(Exception):
    @property
    def message(self):
        return 'An error occurred'

    def __str__(self):
        return self.message
