from django.core.management.base import BaseCommand, CommandError

# import
from funds_CA.models import fundsCA

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # Add data to BDD
        fundsBDD = fundsCA.objects.all()

        for fund in fundsBDD:
        	fund.delete()
