import pandas as pd
import datetime
from pandas_datareader import DataReader
from assets.models import Assets, AssetsInfo
from dateutil.relativedelta import relativedelta
from tqdm import tqdm
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_value_today(asset_historic, last_date_considered):
    logger.info(f'Get asset info: get current value')
    asset = asset_historic.loc[last_date_considered]
    try:
        return asset['Adj Close'], asset['return'], asset['variation']
    except Exception as e:
        logger.info(f'Get asset info: get value today - error: {e}')
        return None, None, None


def get_value_and_variation_over_time(asset_historic, last_date_considered, month=None, day=None):
    logger.info(f'Get asset info: get values over time')

    if month:
        past = (last_date_considered + relativedelta(months=-month))
    elif day:
        past = (last_date_considered + datetime.timedelta(days=-day))
    else:
        raise ValueError('Get value and variation over time: Neither month nor week have been chosen.')
    today = last_date_considered

    logger.info(f'Get asset info: get value over time - past date: {past}')

    try:
        today_value = asset_historic.loc[today]
        past_value = asset_historic.loc[past]
        return past_value['Adj Close'], (today_value['Adj Close'] - past_value['Adj Close']) / (past_value['Adj Close'])
    except Exception as e:
        logger.info(f'Get asset info: get value over time - error: {e}')
        return None, None


def get_asset_info(id_asset, my_assets):
    logger.info(f'Get asset info: get extra info')
    try:
        my_asset = my_assets.loc[id_asset]
        return my_asset['url'], my_asset['name'], my_asset['dividende'], my_asset['date_dividende']
    except Exception as e:
        logger.info(f'Get asset info: get asset info: {e}')
        return None, None, None, None


def insert_value_in_db(id_asset, longname, symbol, asset_historic, my_assets):
    last_date_considered = asset_historic.index[-1]

    asset_value, asset_return, asset_variation = get_value_today(asset_historic=asset_historic,
                                                                 last_date_considered=last_date_considered)
    asset_value_1_week, asset_variation_1_week = get_value_and_variation_over_time(asset_historic=asset_historic,
                                                                                   last_date_considered=last_date_considered,
                                                                                   month=None,
                                                                                   day=7)
    asset_value_1_month, asset_variation_1_month = get_value_and_variation_over_time(asset_historic=asset_historic,
                                                                                     last_date_considered=last_date_considered,
                                                                                     month=1,
                                                                                     day=None)
    asset_value_3_month, asset_variation_3_month = get_value_and_variation_over_time(asset_historic=asset_historic,
                                                                                     last_date_considered=last_date_considered,
                                                                                     month=3,
                                                                                     day=None)

    url, name, dividende, date_dividende = get_asset_info(id_asset=id_asset, my_assets=my_assets)

    logger.info(f'Get asset info: insert in db...')

    response = AssetsInfo.objects.update_or_create(
        id_asset=id_asset,
        defaults={'date': datetime.datetime.today(),
                  'date_update': last_date_considered,
                  'name': name,
                  'url': url,
                  'longname': longname,
                  'symbol': symbol,
                  'value': asset_value,
                  'variation': asset_variation,
                  'asset_return': asset_return,
                  'dividende': dividende,
                  'date_dividende': date_dividende,
                  'value_3_month': asset_value_3_month,
                  'value_1_month': asset_value_1_month,
                  'value_1_week': asset_value_1_week,
                  'var_3_month': asset_variation_3_month,
                  'var_1_month': asset_variation_1_month,
                  'var_1_week': asset_variation_1_week,
                  }
    )
    logger.info(f'Get asset info: ingested in db: {response}')


def get_assets_info_and_insert_in_db():
    df = pd.read_csv('id_all_assets_converted.csv')

    my_assets = pd.DataFrame(Assets.objects.all().values())
    my_assets = my_assets.sort_values(by='date')
    my_assets = my_assets.drop_duplicates(subset=['id_asset'], keep='last')
    my_assets = my_assets.set_index('id_asset')

    start = (datetime.datetime.today() + relativedelta(months=-4)).strftime('%Y-%m-%d')
    end = datetime.datetime.today().strftime('%Y-%m-%d')

    logger.info(f'Get asset info: Getting assets infos on {datetime.datetime.today().strftime("%Y-%m-%d")}')

    iteration = 1

    for index, asset in tqdm(df.iterrows()):

        logger.info(
            f"Get asset info: Getting assets infos for: {asset['longname']} - Iteration {iteration}/{df.shape[0]} ({datetime.datetime.today()})")

        try:
            asset_historic = DataReader(asset['symbol'], "yahoo", start=start, end=end)
            asset_historic['return'] = asset_historic['Adj Close'].diff()
            asset_historic['variation'] = asset_historic['return'] / asset_historic['Adj Close'].shift(1)

            try:
                insert_value_in_db(id_asset=asset['id_asset'], longname=asset['longname'],
                                   symbol=asset['symbol'], asset_historic=asset_historic,
                                   my_assets=my_assets)
            except Exception as e:
                logger.info(f"Get asset info: ERROR: {e}")
        except Exception as e:
            logger.info(f"Get asset info: ERROR: {e}")

        iteration += 1
