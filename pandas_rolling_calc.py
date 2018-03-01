#! python3
# test run rolling calcs.
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = plt.subplot2grid((2, 1), (0, 0))
ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)

data = pd.read_pickle('pickled_df.pickle')

# moving average
# data['TX12MA'] = pd.rolling_mean(data['TX'], 12)
# standard dev
# data['TX12STD'] = pd.rolling_std(data['TX'], 12)
# rolling corr
data_corr = pd.rolling_corr(data['TX'], data['AK'], 12)

# print(data[['TX', 'TX12STD']].head())
data['TX'].plot(ax=ax1, label='TX_data')
data['AK'].plot(ax=ax1, label='AK_data')
data_corr.plot(ax=ax2, label='corr_data')

plt.legend(loc=4)
plt.show()
