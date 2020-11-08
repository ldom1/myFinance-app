from pandas_datareader import DataReader
from pylab import legend, xlabel, ylabel, sqrt, ylim, \
    cov, sqrt, mean, std, plot, show, figure
from numpy import array, zeros, matrix, ones, shape, linspace, hstack, busday_count
import pandas as pd
from numpy.linalg import inv
from tqdm import tqdm
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Portfolio class.
class Portfolio:
    def __init__(self, symbols, start=None, end=None, bench='^GSPC'):

        logger.info(f'Get optimal allocation: class Portfolio')

        # Make sure input is a list
        if type(symbols) != list:
            symbols = [symbols]

        # Create distionary to hold assets.
        self.asset = {}

        nb_of_days_considered_min = int(busday_count(start, end) * .9)

        # Retrieve assets from data source (IE. Yahoo)
        logger.info(f'Get optimal allocation: get assets historic')
        symbols_considered = []
        for symbol in tqdm(symbols):
            try:
                historical_data = DataReader(symbol, "yahoo", start=start, end=end)
                if nb_of_days_considered_min < historical_data.shape[0]:
                    logger.info(
                        f'Get optimal allocation: Select asset with {nb_of_days_considered_min} days min - Asset: {symbol} with {historical_data.shape[0]} days')
                    self.asset[symbol] = historical_data
                    symbols_considered.append(symbol)
                else:
                    logger.info(f'Get optimal allocation: Asset {symbol}.')
                    logger.info(f'Error: Not enough historic')
            except Exception as e:
                logger.info(f'Get optimal allocation: Asset {symbol} not found.')
                logger.info(f'Error: {e}')

        logger.info(f'Get optimal allocation: {len(symbols)} symbols (assets)')

        # Keep only considered symbols
        self.asset = {k: self.asset[k] for k in self.asset if k in symbols_considered}

        # Get Benchmark asset.
        self.benchmark = DataReader(bench, "yahoo", start=start, end=end)
        self.benchmark['Return'] = self.benchmark['Adj Close'].diff()

        # Get returns, beta, alpha, and sharp ratio.
        iteration = 1
        for symbol in symbols_considered:
            logger.info(f'---------')
            logger.info(f'Get optimal allocation: Iteration: {iteration} / {len(symbols_considered)}')
            logger.info(f'Get optimal allocation: Symbol consider: {symbol}')
            self.benchmark = self.benchmark.loc[self.benchmark.index.intersection(self.asset[symbol].index)]
            self.asset[symbol] = self.asset[symbol].loc[self.asset[symbol].index.intersection(self.benchmark.index)]
            logger.info(
                f'Get optimal allocation: {symbol} shape: {self.asset[symbol].shape}, bench shape: {self.benchmark.shape}')

            # Get returns.
            self.asset[symbol]['Return'] = self.asset[symbol]['Adj Close'].diff()
            # Get Beta.
            A = self.asset[symbol]['Return'].fillna(0)
            B = self.benchmark['Return'].fillna(0)

            self.asset[symbol]['Beta'] = cov(A, B)[0, 1] / cov(A, B)[1, 1]

            # Get Alpha
            self.asset[symbol]['Alpha'] = self.asset[symbol]['Return'] - \
                                          self.asset[symbol]['Beta'] * self.benchmark['Return']

            # Get Sharpe Ratio
            tmp = self.asset[symbol]['Return']
            self.asset[symbol]['Sharpe'] = \
                sqrt(len(tmp)) * mean(tmp.fillna(0)) / std(tmp.fillna(0))
            iteration += 1

        self.dates_to_consider = self.benchmark.index

    def nplot(self, symbol, color='b', nval=0):
        tmp = (self.benchmark if symbol == 'bench' else self.asset[symbol])['Adj Close']
        tmp = tmp / tmp[nval]
        tmp.plot(color=color, label=symbol)
        legend(loc='best', shadow=True, fancybox=True)

    def betas(self):
        betas = [v['Beta'][0] for k, v in self.asset.items()]
        return pd.Series(betas, index=self.asset.keys())

    def returns(self):
        returns = [v['Return'].dropna() for k, v in self.asset.items()]
        return pd.Series(returns, index=self.asset.keys())

    def cov(self):
        keys, values = self.returns().keys(), self.returns().values

        values_balanced_in_dates = [y.loc[y.index.intersection(self.dates_to_consider)] for y in values]
        values_balanced_in_dates = [y.values for y in values_balanced_in_dates]

        df = pd.DataFrame(values_balanced_in_dates).T
        df.index = self.dates_to_consider
        df.columns = keys
        return df.cov()

    def get_w(self, kind='sharpe'):
        V = self.cov()
        iV = matrix(inv(V))

        if kind == 'characteristic':
            e = matrix(ones(len(self.asset.keys()))).T
        elif kind == 'sharpe':
            suml = [self.returns()[symbol].sum() for symbol in self.asset.keys()]
            e = matrix(suml).T
        else:
            print('\n  *Error: There is no weighting for kind ' + kind)
            return

        num = iV * e
        denom = e.T * iV * e
        w = array(num / denom).flatten()
        return pd.Series(w, index=self.asset.keys())

    def efficient_frontier_w(self, fp):
        wc = self.get_w(kind='characteristic')
        wq = self.get_w(kind='sharpe')

        fc = self.ret_for_w(wc).sum()
        fq = self.ret_for_w(wq).sum()

        denom = fq - fc
        w = (fq - fp) * wc + (fp - fc) * wq
        return pd.Series(w / denom, index=self.asset.keys())

    def efficient_frontier(self, xi=0.01, xf=4, npts=100, scale=10):
        frontier = linspace(xi, xf, npts)

        i = 0
        rets = zeros(len(frontier))
        sharpe = zeros(len(frontier))
        for f in frontier:
            w = self.efficient_frontier_w(f)
            tmp = self.ret_for_w(w)
            rets[i] = tmp.sum() * scale
            sharpe[i] = mean(tmp) / std(tmp) * sqrt(len(tmp))
            i += 1
        risk = rets / sharpe
        return pd.Series(rets, index=risk), sharpe.max()

    def efficient_frontier_plot(self, xi=0.01, xf=4, npts=100, scale=0.1,
                                col1='b', col2='r', newfig=1, plabel=''):
        eff, m = self.efficient_frontier()

        if newfig == 1:
            figure()

        plot(array(eff.index), array(eff), col1, linewidth=2,
             label="Efficient Frontier " + plabel)
        tmp = zeros(1)
        plot(hstack((tmp, array(eff.index))),
             hstack((0, m * array(eff.index))),
             col2, linewidth=2, label="Max Sharpe Ratio: %6.2g" % m)
        legend(loc='best', shadow=True, fancybox=True)
        xlabel('Risk %', fontsize=16)
        ylabel('Return %', fontsize=16)
        show()

    def min_var_w_ret(self, ret):
        V = self.cov()
        suml = [self.returns()[symbol].sum() for symbol in self.asset.keys()]
        e = matrix(suml).T
        iV = matrix(inv(V))
        num = iV * e * ret
        denom = e.T * iV * e
        return pd.Series(array(num / denom).flatten(), index=self.asset.keys())

    def ret_for_w(self, w):
        tmp = self.returns()
        tmpl = [v * wi for v, wi in zip(tmp.values, w)]
        return pd.Series(tmpl, index=tmp.keys()).sum()
