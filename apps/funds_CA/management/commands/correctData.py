from django.core.management.base import BaseCommand, CommandError

# import
from datetime import date
from funds_CA.models import fundsCA

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # Add data to BDD
        fundsBDD = fundsCA.objects.all()

        for fund in fundsBDD:
        	fund.date = date(fund.date.year, fund.date.month, fund.date.day)
        	fund.save()
