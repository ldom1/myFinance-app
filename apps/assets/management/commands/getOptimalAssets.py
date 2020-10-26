from django.core.management.base import BaseCommand, CommandError

# import
import pandas as pd
import datetime
from assets.scripts.get_optimal_assets import get_optimal_assets

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # Get Optimal data on all assets
        df = pd.read_csv('id_asset_converted.csv')
        df = df.sample(frac=1)
        df = df.iloc[:15]

        logger.info('Get optimal allocation: Data imported')
        logger.info(f'Get optimal allocation: {df.shape[0]} assets')

        start = '2020-06-01'
        end = datetime.datetime.today().strftime('%Y-%m-%d')

        get_optimal_assets(df=df, start=start, end=end)
