import  pandas as pd
import numpy as np

df_7 = pd.DataFrame({'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                     'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                     'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                     'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']})


df_7_new = df_7[df_7['age']>2]
df_7_new = df_7_new[df_7_new['priority'] == 'no' ]
print(df_7_new)