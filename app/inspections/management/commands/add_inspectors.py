import csv

from django.core.management.base import BaseCommand

from ...models import Post, Inspector


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/docs/officers.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                name=row[0].replace("\n", "").lower()
                post_id=Post.objects.get(name=row[1].replace("\n", "").lower().strip()).pk
                # print(name, post_d)
                Inspector.objects.get_or_create(
                    name=name,
                    post=Post.objects.get(id=post_id),
                )
                self.stdout.write(self.style.SUCCESS(f"{name} added"))