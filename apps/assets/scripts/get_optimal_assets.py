from pylab import *

from assets.scripts.quantpy.portfolio import Portfolio

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_optimal_assets(df, start, end):
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

    print(df_res)
