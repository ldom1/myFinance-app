from django.core.management.base import BaseCommand, CommandError

# import
from code.assets.get_assets_infos import get_assets_info_and_insert_in_db


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # Add data to BDD
        get_assets_info_and_insert_in_db()
