from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class BaseWeatherEntity:
    created_at: datetime = field(
        default_factory=lambda: datetime.now(),
        kw_only=True
    )
