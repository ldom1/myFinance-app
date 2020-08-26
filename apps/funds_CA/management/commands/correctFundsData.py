from django.core.management.base import BaseCommand, CommandError
from datetime import date

from apps.funds_ca.models import fundsCA


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # Add data to BDD
        funds_db = fundsCA.objects.all()

        for fund in funds_db:
            fund.date = date(fund.date.year, fund.date.month, fund.date.day)
            fund.save()
