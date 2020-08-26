from django.core.management.base import BaseCommand, CommandError

# import
from funds_CA.scripts.getFundsCA import getFundsData

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # Add data to BDD
        getFundsData()
