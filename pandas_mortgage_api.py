#! python3
# test run joining multiple data sources.
import pandas as pd
import quandl
import pickle

api_key = open('quandl_api_key.txt', 'r').read()


def load_hpi_data():
    data = pd.read_csv('newcsv4.csv')
    data.set_index('Date', inplace=True)
    benchmark = (data['United States seasonaly adjusted'] - data['United States seasonaly adjusted']
                 [0]) / data['United States seasonaly adjusted'][0] * 100.0
    benchmark = pd.DataFrame(benchmark)
    benchmark.index = pd.to_datetime(benchmark.index)
    # benchmark = benchmark.resample('M').mean()
    return benchmark


def mortgage_30yr():
    df = quandl.get("FRED/WMORTG", authtoken=api_key, start_date="1975-01-01")
    df['VALUE'] = (df['VALUE'] - df['VALUE'][0]) / df['VALUE'][0] * 100.0
    df = df.resample('M').mean()
    return df


def us_unemployment():
    df = quandl.get("USMISERY/INDEX", authtoken=api_key, start_date="1975-01-01")
    df["Unemployment Rate"] = (df["Unemployment Rate"]-df["Unemployment Rate"]
                               [0]) / df["Unemployment Rate"][0] * 100.0
    df = df.resample('M').mean()
    df = pd.DataFrame(df['Unemployment Rate'])
    return df


m30 = mortgage_30yr()
bench = load_hpi_data()
unemp = us_unemployment()

joined_data = bench.join([unemp, m30])

joined_data.to_pickle('joined_data.pickle')
