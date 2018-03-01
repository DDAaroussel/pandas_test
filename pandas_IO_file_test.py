#! python3
# test run of reading from and outputting to csv.
import pandas as pd

df = pd.read_csv('test_data.csv')
df.set_index('date', inplace=True)
# print(df)
# df.to_csv('newcsv.csv')
#
# df = pd.read_csv('newcsv.csv', index_col=0)
# print(df.head())
# df.columns = ['price_test']
# print(df)
# df.to_csv('newcsv2.csv')
# df.to_csv('newcsv3.csv', header=False)
#
# df = pd.read_csv('newcsv3.csv', names=['date', 'price_test'], index_col=0)
# print(df)
#
# df.to_html('example.html')

df = pd.read_csv('newcsv3.csv', names=['date', 'price'])
print(df.head())
df.rename(columns={'price': 'value'}, inplace=True)
print(df)
