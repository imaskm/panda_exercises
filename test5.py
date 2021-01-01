import pandas as pd
import numpy as np

data = {'name': ['Jack', np.nan, 'Anna', 'Michael', 'Vanessa', 'Andrew', 'Monica'],
        'surname': ['Snow', np.nan, 'Scott', 'Jordna', 'Willis', 'Hughes', 'Dee'],
        'age': [31, np.nan, 23, 26, 21, 28, 24],
        'sex': ['m', np.nan, 'f', 'm', 'f', 'm', 'f'],
        'quiz1': [71, np.nan, np.nan, 65, 59, 61, 73],
        'quiz2': [85, np.nan, np.nan, 76, 68, 65, 80]}
df = pd.DataFrame(data)
# print(df.isnull())
df = df.dropna(how='all')

df['quiz1'].fillna(df['quiz1'].mean(), inplace=True)

df['quiz2'].fillna(method="bfill", inplace=True)

print(df)
