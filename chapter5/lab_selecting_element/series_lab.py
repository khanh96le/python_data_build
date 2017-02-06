import pandas as pd
from pandas import DataFrame, Series

pop = {
    'Ohio': {
        2001: 2.4,
        2002: 2.9
    },
    'Nevada': {
        2000: 1.5,
        2001: 1.7,
        2002: 3.6
    }
}

df = DataFrame(pop)
df.index.name = 'year'
df.columns.name = 'state'

print df
