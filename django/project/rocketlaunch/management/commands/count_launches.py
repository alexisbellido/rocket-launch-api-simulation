from django.core.management.base import BaseCommand
from rocketlaunch.models import Launch, Location


class Command(BaseCommand):
    help = "Count launches with loop."

    def add_arguments(self, parser):
        parser.add_argument(
            '--top', 
            dest="top",
            type=int,
            default=10,
            help='Number of top locations to retrieve.')

    def handle(self, *args, **options):
        top = options.get('top')
        launches = Launch.objects.all()
        counter = {}
        for launch in launches:
            if launch.location.id in counter:
                counter[launch.location.id] += 1
            else:
                counter[launch.location.id] = 0

        top_count = 0
        result = []
        for location_id, location_count in sorted(counter.items(), key=lambda item: item[1], reverse=True):
            self.stdout.write(
                self.style.SUCCESS(
                    f"location_id: {location_id}, location_count: {location_count}."
                )
            )
            location = Location.objects.get(id=location_id)
            result.append({
                "id": location_id,
                "count": location_count,
                "location": location,
            })
            top_count += 1
            if top_count == top:
                break
        print(result)
