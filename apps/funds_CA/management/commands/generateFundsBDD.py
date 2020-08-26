from django.core.management.base import BaseCommand, CommandError
from funds_CA.models import fundsCA

from code.funds_CA.get_funds_ca_values import get_all_funds_ca_data_and_ingest_in_db


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # Add data to BDD
        get_all_funds_ca_data_and_ingest_in_db(model_db=fundsCA)
