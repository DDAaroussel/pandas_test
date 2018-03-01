#! python3
# test run missing data (NaN).
import pandas as pd

data = pd.read_pickle('pickled_df.pickle')

data.dropna(inplace=True)  # This removes NaN
data.dropna(how='all', inplace=True)  # different drop options
data.fillna(method='ffill', inplace=True)  # forward fill, using previous record's value
# some people fillna with high values (999) so that ML classifiers
# automatically filter our outliers.
data.isnull().values.sum()  # the count of all NaN values.
