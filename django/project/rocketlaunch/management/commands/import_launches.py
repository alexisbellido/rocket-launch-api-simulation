import csv
from django.core.management.base import BaseCommand
# from rocketlaunch.models import Launch


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
                    cost = row["mission_cost"]
                    time_date = row["launch_time_date"]
                    company_id = row["rocket_company_id"]
                    status_id = row["mission_status_id"]
                    location_id = row["launch_location_id"]
                    # _, created = Launch.objects.get_or_create(
                    #     id=id,
                    #     name=name
                    # )
                    # if created:
                    #     action = "created"
                    # else:
                    #     action = "updated"
                    print(
                        id,
                        name,
                        cost,
                        time_date,
                        company_id,
                        status_id,
                        location_id
                    )
                    # self.stdout.write(
                    #     self.style.SUCCESS(
                    #         f"Launch successfully {action}: {id} {name}"
                    #     )
                    # )
        else:
            self.stderr.write(
                self.style.WARNING(
                    "Please provide a path for the input file."
                )
            )
