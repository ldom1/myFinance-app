from pylab import *
import pandas as pd
from tqdm import tqdm
from assets.scripts.src.quantpy.portfolio import Portfolio
from assets.models import AssetsInfo, OptimalAssetsInfo

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add_current_asset_info(df):
    asset_info_df = pd.DataFrame(AssetsInfo.objects.all().values())
    asset_info_df = asset_info_df.dropna(subset=['id_asset'])
    asset_info_df_latest = asset_info_df[asset_info_df.date_update == asset_info_df.date_update.max()]

    asset_info_df_latest = asset_info_df_latest.drop(['id'], axis=1)

    logger.info(f'Get optimal allocation: add asset info - initial shape: {df.shape}')
    df = df.merge(asset_info_df_latest, on='id_asset', how='inner')
    logger.info(f'Get optimal allocation: add asset info - result shape: {df.shape}')
    return df


def insert_df_in_db(df):
    logger.info(f'Insert df in db: Start ...')
    logger.info(f'Insertion of : {df.shape[0]} rows')

    for index, row in tqdm(df.iterrows()):
        try:
            if row['id_asset']:
                OptimalAssetsInfo.objects.get_or_create(
                    date_update=row['date_update'],
                    id_asset=row['id_asset'],
                    name=row['name'],
                    exchange=row['exchange'],
                    shortname=row['shortname'],
                    quoteType=row['quoteType'],
                    symbol=row['symbol'],
                    index=row['index'],
                    score=int(row['score']),
                    typeDisp=row['typeDisp'],
                    longname=row['longname'],
                    weight=row['weight'],
                    betas=row['betas'],
                    weight_low_var=row['weight_low_var'],
                    value=row['value'],
                    variation=row['variation'],
                    dividende=row['dividende'],
                    value_3_month=row['value_3_month'],
                    value_1_month=row['value_1_month'],
                    value_1_week=row['value_1_week'],
                    var_3_month=row['var_3_month'],
                    var_1_month=row['var_1_month'],
                    var_1_week=row['var_1_week']
                )
        except Exception as e:
            logger.info(f'Get optimal allocation: error while inserting rows: {e}')


def get_optimal_assets(df, start, end, nb_assets_selected, previously_selected):
    asset_symbols = list(df['symbol'])

    logger.info(f'Get optimal allocation: start date: {start}')
    logger.info(f'Get optimal allocation: end date: {end}')
    P = Portfolio(symbols=asset_symbols, start=start, end=end, bench='^GSPC')

    # Add weight
    optimal_weight = P.get_w()
    optimal_weight = optimal_weight.reset_index()
    optimal_weight.columns = ['symbol', 'weight']

    # Add betas
    betas = P.betas()
    betas = betas.reset_index()
    betas.columns = ['symbol', 'betas']

    # Find the optimal weighting that yields the same return with minimum variance.
    bb = P.ret_for_w(ones(len(asset_symbols)))
    mm = cumsum(bb)[-1]
    optimal_weight_low_var = P.min_var_w_ret(mm)
    optimal_weight_low_var = optimal_weight_low_var.reset_index()
    optimal_weight_low_var.columns = ['symbol', 'weight_low_var']

    df_res = df.merge(optimal_weight, on=['symbol'], how='inner')
    df_res = df_res.merge(betas, on=['symbol'], how='inner')
    df_res = df_res.merge(optimal_weight_low_var, on=['symbol'], how='inner')
    df_res = df_res.sort_values(by='weight_low_var', ascending=False)

    df_res = add_current_asset_info(df=df_res)

    logger.info(f'Get optimal allocation: Done.')

    logger.info(f'Get optimal allocation: Sort values by weight and select {nb_assets_selected} first.')
    df_res = df_res.sort_values(by='weight', ascending=False)
    df_res = df_res.iloc[:nb_assets_selected]
    df_res['previously_selected'] = previously_selected

    df_res.to_csv(f'test_optim_{str(previously_selected)}.csv', index=False, header=True)

    insert_df_in_db(df=df_res)
