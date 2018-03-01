#! python3
# test run of API -> data frame.
import pandas as pd
import quandl
api_key = open('quandl_api_key.txt', 'r').read()
df = quandl.get("FMAC/HPI", authtoken=api_key)
print(df.head())
df.to_csv('newcsv4.csv')
