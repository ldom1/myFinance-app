from django.core.management.base import BaseCommand, CommandError
from assets.models import Assets

from code.assets.get_assets_values import get_all_assets_ca_data_and_ingest_in_db


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # Add data to BDD
        get_all_assets_ca_data_and_ingest_in_db(model_db=Assets)
