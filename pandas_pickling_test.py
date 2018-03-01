#! python3
# test run pickling.
import pandas as pd
import pickle

# the df we want to pickle
to_pickle_df = pd.read_csv('newcsv4.csv')

# output to a pickle df
pickle_out = open('pickled_df.pickle', 'wb')
pickle.dump(to_pickle_df, pickle_out)
pickle_out.close()

# now read the pickled df
pickle_in = open('pickled_df.pickle', 'rb')
after_pickle_df = pickle.load(pickle_in)
print(after_pickle_df)

# using pandas pickle is simpler
to_pickle_df.to_pickle('pandas_pickle.pickle')
after_pickle_df2 = pd.read_pickle('pandas_pickle.pickle')
