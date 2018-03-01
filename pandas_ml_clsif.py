#! python3
# test run mapping functions and ml classif.
import pandas as pd
import numpy as np
import quandl
import pickle
from statistics import mean
from sklearn import svm, preprocessing, cross_validation


def create_labels(cur_hpi, fut_hpi):  # cur_hpi = US seasonally adjusted, fut_hpi = US_HPI_Future
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0


data = pd.read_pickle('joined_data.pickle')
data_pct = data.pct_change()
data_pct = data_pct.replace([np.inf, -np.inf], np.nan)
data_no_na = data_pct.dropna(how='any')  # about 200 NA records

data_no_na['US_HPI_Future'] = data_no_na['United States seasonaly adjusted'].shift(-1)
data_no_na['label'] = list(
    map(create_labels, data_no_na['United States seasonaly adjusted'], data_no_na['US_HPI_Future']))

x = np.array(data_no_na.drop(['label', 'US_HPI_Future'], 1))
x = preprocessing.scale(x)
y = np.array(data_no_na['label'])

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)

clf = svm.SVC(kernel='linear')
clf.fit(x_train, y_train)

print(clf.score(x_test, y_test))
