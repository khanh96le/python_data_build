import pandas as pd
from pandas import DataFrame, Series
import pandas.io.data as web

all_data = {}
for ticket in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
  all_data[ticket] = web.get_data_yahoo(ticket, '1/1/2000', '1/1/2015')
price = DataFrame(
  {tic: data['Adj Close']} for tic, data in all_data.iteritems()
)
volume = DataFrame(
  {tic: data['Volume']} for tic, data in all_data.iteritems()
)

print 0