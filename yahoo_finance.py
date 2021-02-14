#get historical market data from YFinance(Yahoo Finance) API

import yfinance as yf

target_stocks=['run','penn','sedg','sam','qdel','halo','cree','gnrc','sail','iivi',\
              'nvax','vxrt','gnpx','veri','celh','plug','codx','nls','grwg','awh',\
              'aapl','msft','nke','crm','dis','cat','hd','wmt','hon','unh']
for item in range(len(target_stocks)):
    yf_data=target_stocks[item]+'_yf.csv'
    df = yf.download(tickers="{}".format(target_stocks[item]), start='2020-01-01', end='2021-01-01')
    df.to_csv(yf_data, index=False) 

#read csv to a dictionary of dataframes 
d = {}  # dictionary that will hold the dataframes 
for name in target_stocks:  # loop over files
    d[name] = pd.read_csv(name+"_yf.csv")
    d[name]['return']=d[name]['Close']-d[name]['Open']
    d[name]['log_return']=np.log(d[name]['Close'])-np.log(d[name]['Open'])
#check missing values    
    print(d[name].isnull().values.any())
