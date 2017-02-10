import pandas as pd
from pandas import DataFrame
import numpy as np


df1 = DataFrame(
    np.arange(6).reshape(3,2),
    index=['a', 'b', 'c'],
    columns=['one', 'two']
)

df2 = DataFrame(
    np.arange(4).reshape(2,2),
    index=['a', 'c'],
    columns=['three', 'four']
)

data = pd.concat(
    [df1, df2],
    axis=1,
    keys=['level1', 'level2'],
    names=['upper', 'lower']
)

print 0
