import json
from django.core.management.base import BaseCommand
from core.apps.weather.models import City


class Command(BaseCommand):
    help = 'Import cities from a JSON file'

    def handle(self, *args, **kwargs):
        with open('cities.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                City.objects.create(name=item['city'])
        self.stdout.write(self.style.SUCCESS('Successfully imported cities'))
