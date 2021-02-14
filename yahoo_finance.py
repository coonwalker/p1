#get historical market data from Yahoo Finance API

import yfinance as yf

target_stocks=['run','penn','sedg','sam','qdel','halo','cree','gnrc','sail','iivi',\
              'nvax','vxrt','gnpx','veri','celh','plug','codx','nls','grwg','awh',\
              'aapl','msft','nke','crm','dis','cat','hd','wmt','hon','unh']
for item in range(len(target_stocks)):
    yf_data=target_stocks[item]+'_yf.csv'
    df = yf.download(tickers="{}".format(target_stocks[item]), start='2020-01-01', end='2021-01-01')
    df.to_csv(yf_data, index=False) 
