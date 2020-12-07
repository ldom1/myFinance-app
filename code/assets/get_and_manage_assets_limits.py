import pandas as pd
import datetime
from pandas_datareader import DataReader
from assets.models import AssetsInfo, AssetsCheckLimits
from tqdm import tqdm
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add_assets_info_to_assets_check_limit():
    iteration = 1
    for asset_info in tqdm(AssetsInfo.objects.all()):

        logger.info(f"Add asset info in asset check limits: {asset_info.name} ({datetime.datetime.today()})")

        if AssetsCheckLimits.objects.filter(id_asset=asset_info.id_asset).exists():
            logger.info(f"Add asset info in asset check limits: {asset_info.name} already exists")
        else:
            AssetsCheckLimits.objects.get_or_create(
                date=datetime.datetime.today(),
                date_update=asset_info.date_update,
                id_asset=asset_info.id_asset,
                name=asset_info.name,
                symbol=asset_info.symbol,
                longname=asset_info.longname,
                down_limit=None,
                down_limit_knocked=False,
                up_limit=None,
                up_limit_knocked=False,
            )
        logger.info(f'Add asset info in asset check limits: asset added')


def get_asset_value(symbol):
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    asset_historic = DataReader(symbol, "yahoo", start=today, end=today)
    return asset_historic['Adj Close'].values[0]


def update_up_limit():
    assets_limits = AssetsCheckLimits.objects.filter(up_limit__isnull=False)

    for asset in assets_limits:

        logger.info(f"Get and check asset limits: update up limit: {asset.longname}")

        asset_value = get_asset_value(asset.symbol)

        if asset_value >= asset.up_limit:
            logger.info(
                f"Get and check asset limits: up limit knocked: current value: {asset_value} - limit {asset.up_limit}")
            asset.up_limit_knocked = True
            asset.save()


def update_down_limit():
    assets_limits = AssetsCheckLimits.objects.filter(down_limit__isnull=False)

    for asset in assets_limits:

        logger.info(f"Get and check asset limits: update down limit: {asset.longname}")

        asset_value = get_asset_value(asset.symbol)

        if asset_value <= asset.down_limit:
            logger.info(
                f"Get and check asset limits: down limit knocked: current value: {asset_value} - limit {asset.down_limit}")
            asset.down_limit_knocked = True
            asset.save()


def update_limits():
    update_up_limit()
    update_down_limit()
