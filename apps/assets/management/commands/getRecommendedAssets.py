from django.core.management.base import BaseCommand

# import
import pandas as pd
import datetime
from code.assets.get_recommended_assets_by_analyts import get_code_and_insert_in_db

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # Get recommended assets
        get_code_and_insert_in_db()
