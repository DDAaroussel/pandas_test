#! python3
# test run pickling.
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

data = pd.read_pickle('pickled_df.pickle')
# compute the percent change the last column in the data frame.
# benchmark = (data['United States seasonaly adjusted'] - data['United States seasonaly adjusted']
#              [0]) / data['United States seasonaly adjusted'][0] * 100.0
#
# fig = plt.figure()
# ax1 = plt.subplot2grid((1, 1), (0, 0))
#
# data.plot(ax=ax1)  # The other columns actually need to have their % change calculated.
# benchmark.plot(ax=ax1, color='k', linewidth=10)
#
# plt.legend().remove()
# plt.show()

# correlation
data_correl = data.corr()
# print(data_correl)
print(data_correl.describe())
