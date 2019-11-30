from django.core.management.base import BaseCommand, CommandError

# import
import time
from pea.scripts.managePEA import valorise_order, valorise_pea, risk_pea, generateHistory

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # Add data to BDD
        valorise_order()
        time.sleep(10)
        valorise_pea()
        risk_pea()
        time.sleep(10)
        generateHistory()