#! python3
# test run resampling.
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

data = pd.read_pickle('pickled_df.pickle')

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

tx1yr = data['TX'].resample('A')  # This needs to be a year index however.
print(tx1yr.head())

data['TX'].plot(ax=ax1)
tx1yr.plot(ax=ax1)

plt.legend().remove()
plt.show()
