import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# import data
def get_data(stocks, start, end):
    stockData = pdr.get_data_yahoo(stocks, start, end)
    stockData = stockData['Close']
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix
stocks = ['CBA', 'BHP', 'TLS', 'NAB.AX', 'WBC.AX', 'STO.AX']
# stocks = [stock + '.AX' for stock in stockList]
endDate = datetime.now().date()
startDate = endDate - timedelta(days=300)
meanReturns, covMatrix = get_data(stocks, startDate, endDate)
print(meanReturns)