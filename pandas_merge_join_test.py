#! python3
# test run merging and joining data frame.
import pandas as pd

df1 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55],
                    'Year': [2001, 2002, 2003, 2004]})

df2 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Unemployment': [7, 8, 9, 6],
                    'Low_tier_HPI': [50, 52, 50, 53],
                    'Year': [2001, 2003, 2004, 2005]})

# you might want to use merge if you've got multiple
# tables that share a single primary key like user_id

# merged = pd.merge(df1, df3, on='Year', how='outer')
# merged.set_index('Year', inplace=True)
# print(merged)

# to use a SQL like index use join instead.
joined = df1.set_index('Year').join(df3.set_index('Year'), how='outer', lsuffix='a', rsuffix='b')
print(joined)

# In this case, both the outer merge and outer join produce
# the same output
