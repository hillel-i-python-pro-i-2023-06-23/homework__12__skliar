from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll

class GenerateNumbers(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--amount",
            type=int,
            help="how many phones will we generated",
            default=10,
        )

    def handle(self, *args, **options):
        amount: int = options['amount']
        print(f"{amount}")