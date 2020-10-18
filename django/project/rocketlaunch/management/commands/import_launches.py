import csv
import datetime
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from rocketlaunch.models import Launch


class Command(BaseCommand):
    help = "Import launches"

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
                    name = row["mission_name"]
                    try:
                        cost = int(row["mission_cost"])
                    except ValueError:
                        cost = None
                    time_date_obj = make_aware(
                        datetime.datetime.strptime(
                            row["launch_time_date"],
                            '%Y-%m-%d %H:%M:%S'
                        )
                    )
                    # Use foreign key value directly for
                    # company_id, status_id, location_id
                    company_id = row["rocket_company_id"]
                    status_id = row["mission_status_id"]
                    location_id = row["launch_location_id"]
                    _, created = Launch.objects.get_or_create(
                        id=id,
                        name=name,
                        cost=cost,
                        time_date=time_date_obj,
                        company_id=company_id,
                        status_id=status_id,
                        location_id=location_id
                    )
                    if created:
                        action = "created"
                    else:
                        action = "updated"
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Launch successfully {action}: {id} {name}."
                        )
                    )
        else:
            self.stderr.write(
                self.style.WARNING(
                    "Please provide a path for the input file."
                )
            )
