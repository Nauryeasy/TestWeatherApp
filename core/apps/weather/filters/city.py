from dataclasses import dataclass, field


@dataclass(frozen=True)
class CityFilters:
    name: str = field(default=None)
    search: str = field(default=None)
