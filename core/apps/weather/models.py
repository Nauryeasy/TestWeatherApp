from django.db import models

from core.apps.weather.entities.city import City as CityEntity


class City(models.Model):
    name = models.CharField(max_length=255)
    count_requests = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def to_entity(self) -> CityEntity:
        return CityEntity(
            id=self.id,
            name=self.name,
            count_requests=self.count_requests
        )

    def __str__(self):
        return self.name
