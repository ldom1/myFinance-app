from django.core.management.base import BaseCommand, CommandError

# import
from pea.models import *

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # Add data to BDD
        orders = Order.objects.all()

        for order in orders:
        	order.delete()
