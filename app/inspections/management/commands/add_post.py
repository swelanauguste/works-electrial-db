import csv

from django.core.management.base import BaseCommand

from ...models import Post


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/docs/officers.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                name = row[1].replace("\n", "").lower().strip()
                Post.objects.get_or_create(
                    name=name,
                )
                self.stdout.write(self.style.SUCCESS(f"{name} added"))