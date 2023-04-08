import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader
from pandas_datareader import data as pdr

# import data
def get_data(stocks, start, end):
    stockData= pdr.get_data_yahoo(stocks, start, end)
    stockData = stockData['Close']
    returns= stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix= returns.cov()
    return meanReturns, covMatrix 

stockList= ['CBA', 'BHP', 'TLS', 'NAB', 'WBC', 'STO']

stocks= [stocks+ ' .AX' for stocks in stockList]
endDate= dt.datetime.now()
startDate= endDate- dt.timedelta(days=300)

meanReturns, covMatrix = get_data( stocks, startDate, endDate)

print(meanReturns)