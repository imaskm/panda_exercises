import pandas as pd

df_9_1 = pd.DataFrame({'name': ['Jason', 'Tina', 'Jake', 'Amy'],
                     'age': [32, 28, 23, 33],
                     'TestScore': [70, 92, 88, 65]})
df_9_2 = pd.DataFrame({'name': ['Tim', 'Alice'],
                     'age': [21, 33],
                     'TestScore': [81, 83]})

res = pd.concat([df_9_1,df_9_2])

print(res)