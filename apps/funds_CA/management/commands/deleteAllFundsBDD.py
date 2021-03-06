from django.core.management.base import BaseCommand, CommandError

from apps.funds_CA.models import fundsCA


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # Add data to BDD
        funds_db = fundsCA.objects.all()

        for fund in funds_db:
            fund.delete()
