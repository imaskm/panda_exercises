import pandas as pd

df1 = pd.DataFrame({'city': ['Chicago', 'San Francisco', 'New York City'], 'rank': range(1, 4)})
df2 = pd.DataFrame({'city': ['Chicago', 'Boston', 'Los Angeles'], 'rank': [1, 4, 5]})

res = pd.merge(df1,df2)
res = pd.concat([df1,df2],axis=1,join="inner")
print(res)