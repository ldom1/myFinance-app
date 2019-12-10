from django.core.management.base import BaseCommand, CommandError

# import
from assets.models import Assets

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # Add data to BDD
        assets = Assets.objects.all()

        for asset in assets:
        	asset.delete()
