import csv

from django.core.management.base import BaseCommand

from ...models import Location


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/docs/locations.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                name = row[0].replace("\n", "").lower()
                Location.objects.get_or_create(
                    name=name,
                )
                self.stdout.write(self.style.SUCCESS(f"{name} added"))