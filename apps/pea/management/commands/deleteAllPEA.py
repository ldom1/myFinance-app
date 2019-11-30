from django.core.management.base import BaseCommand, CommandError

# import
from pea.models import *

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # Add data to BDD
        pea = PEA.objects.all()
        orders = Order.objects.all()

        for p in pea:
        	p.delete()

        for order in orders:
        	order.delete()
