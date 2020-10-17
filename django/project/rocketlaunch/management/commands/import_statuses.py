import csv
from django.core.management.base import BaseCommand
from rocketlaunch.models import Status


class Command(BaseCommand):
    help = "Import statuses"

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
                    status = row["status"]
                    _, created = Status.objects.get_or_create(
                        id=id,
                        status=status
                    )
                    if created:
                        action = "created"
                    else:
                        action = "updated"
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Status successfully {action}: {id} {status}"
                        )
                    )
        else:
            self.stderr.write(
                self.style.WARNING(
                    "Please provide a path for the input file."
                )
            )
