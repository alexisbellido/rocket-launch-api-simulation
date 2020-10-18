from django.core.management.base import BaseCommand
from django.db.models import Count
from rocketlaunch.models import Launch, Location


class Command(BaseCommand):
    help = "Count launches with loop and Django's annotate to compare."

    def add_arguments(self, parser):
        parser.add_argument(
            '--top',
            dest="top",
            type=int,
            default=10,
            help='Number of top locations to retrieve.')

    def handle(self, *args, **options):
        top = options.get('top')

        # counting with loop
        launches = Launch.objects.all()
        counter = {}
        for launch in launches:
            # this is a more Pythonic alternative to the if/else block below
            counter[launch.location.id] = counter.setdefault(
                launch.location.id,
                0
            ) + 1
            # if launch.location.id in counter:
            #     counter[launch.location.id] += 1
            # else:
            #     counter[launch.location.id] = 1

        top_count = 0
        result = []
        self.stdout.write("Counting with loop...")
        for location_id, count_launches in sorted(
            counter.items(),
            key=lambda item: item[1],
            reverse=True
        ):
            self.stdout.write(
                self.style.SUCCESS(
                    f"location_id {location_id} [{count_launches}]"
                )
            )
            location = Location.objects.get(id=location_id)
            result.append({
                "id": location_id,
                "count": count_launches,
                "location": location,
            })
            top_count += 1
            if top_count == top:
                break
        print(result)

        self.stdout.write("Counting with Django's annotate...")
        locations = Location.objects.annotate(
            count_launches=Count('launch__id')
        ).order_by('-count_launches')[:top]
        for location in locations:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{location.location} | "
                    f"location_id {location.id} [{location.count_launches}]"
                )
            )
