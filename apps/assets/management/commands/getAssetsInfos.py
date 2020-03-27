from django.core.management.base import BaseCommand, CommandError

# import
from assets.scripts.getAssetsInfos import get_asset_info

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # Add data to BDD
        get_asset_info()
