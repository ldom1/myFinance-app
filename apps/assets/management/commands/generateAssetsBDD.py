from django.core.management.base import BaseCommand, CommandError

# import
from assets.scripts.getAssets import getAssetData

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # Add data to BDD
        getAssetData()
