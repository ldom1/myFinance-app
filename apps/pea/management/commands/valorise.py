from django.core.management.base import BaseCommand, CommandError

# import
from pea.scripts.valorise import valorise_order, valorise_pea

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # Add data to BDD
        valorise_order()
        valorise_pea()
