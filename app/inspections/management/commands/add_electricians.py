import csv

from django.core.management.base import BaseCommand

from ...models import Post, Inspector


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/docs/electricians.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                name=row[0].lower()
                licence_no=row[1].lower()
                phone=row[2].lower().strip()
                Inspector.objects.get_or_create(
                    name=name,
                    licence_no=licence_no,
                    phone=phone,
                )
                self.stdout.write(self.style.SUCCESS(f"{name} added"))