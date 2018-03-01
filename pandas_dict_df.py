#! python3
# test run of the pandas library.
# convert dictionary to data frame.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# create a dictionary, which we will convert to df
web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 53, 43, 45, 64, 34],
             'Bounce_Rate': [65, 72, 62, 64, 54, 66]}

df = pd.DataFrame(web_stats)

df.set_index('Day', inplace=True)
# print(df)
# print(df['Visitors'])
# print(df.Visitors)
# print(df[['Bounce_Rate', 'Visitors']])
# print(df.Visitors.tolist())
# print(np.array(df[['Bounce_Rate', 'Visitors']]).tolist())
df2 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))
print(df2)
