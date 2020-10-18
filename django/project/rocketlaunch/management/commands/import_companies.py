import csv
from django.core.management.base import BaseCommand
from rocketlaunch.models import Company


class Command(BaseCommand):
    help = "Import companies"

    def add_arguments(self, parser):
        parser.add_argument(
            "--input",
            dest="input_path",
            default=None,
            help="Input file path.",
        )

    def handle(self, *args, **options):
        input_path = options.get("input_path")
        if input_path:
            with open(input_path, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    id = row["id"]
                    name = row["name"]
                    _, created = Company.objects.get_or_create(
                        id=id,
                        name=name
                    )
                    if created:
                        action = "created"
                    else:
                        action = "updated"
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Company successfully {action}: {id} {name}."
                        )
                    )
        else:
            self.stderr.write(
                self.style.WARNING(
                    "Please provide a path for the input file."
                )
            )
