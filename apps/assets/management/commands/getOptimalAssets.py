from django.core.management.base import BaseCommand, CommandError

# import
import pandas as pd
import datetime
from apps.assets.scripts.get_optimal_assets import get_optimal_assets

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # Get Optimal data on all assets
        start = '2017-06-01'
        end = datetime.datetime.today().strftime('%Y-%m-%d')
        nb_assets_selected = 10

        df = pd.read_csv('id_all_assets_converted.csv')

        logger.info('Get optimal allocation for all assets: Data imported')
        logger.info(f'Get optimal allocation for all assets: {df.shape[0]} assets')

        get_optimal_assets(df=df, start=start, end=end, nb_assets_selected=nb_assets_selected,
                           previously_selected=False)

        df = pd.read_csv('id_selected_assets_converted.csv')

        logger.info('Get optimal allocation for selected assets: Data imported')
        logger.info(f'Get optimal allocation for selected assets: {df.shape[0]} assets')

        get_optimal_assets(df=df, start=start, end=end, nb_assets_selected=nb_assets_selected, previously_selected=True)
