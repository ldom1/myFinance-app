from django.core.management.base import BaseCommand, CommandError

# import
from code.assets.get_and_manage_assets_limits import add_assets_info_to_assets_check_limit, update_limits


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # Add data to BDD
        add_assets_info_to_assets_check_limit()
        update_limits()
