# import logging

from django.core.management.base import BaseCommand

from applications.fill_contacts.models import PhoneUser
from applications.fill_contacts.services.generate_users import generate_users


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--amount",
            type=int,
            help="how many phones will we generated",
            default=10,
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]

        # logger = logging.getLogger("django")

        queryset = PhoneUser.objects.all()
        # logger.info(f"Current amount of users before: {queryset.count()}")
        for user in generate_users(amount=amount):
            user.is_auto_generate = True
            user.save()
        self.stdout.write(self.style.SUCCESS(f"Have {queryset.count()} users"))
        # logger.info(f"Current amount of users after: {queryset.count()}")
