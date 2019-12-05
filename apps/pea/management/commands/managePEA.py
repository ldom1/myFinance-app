from django.core.management.base import BaseCommand, CommandError

# import
import time
from pea.scripts.managePEA import valorise_order, valorise_pea, risk_pea, generateHistory, variationInterdayPeaValue

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # Functions
        #valorise_order()
        time.sleep(10)
        valorise_pea()
        #risk_pea()
        time.sleep(10)
        variationInterdayPeaValue()
        time.sleep(10)
        generateHistory()

