import pandas as pd

df1 = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                    'key2': ['one', 'one', 'one', 'two'],
                    'lval': [4, 5, 6, 7]})
df2 = pd.DataFrame({'key3': ['foo', 'foo', 'bar'],
                    'key4': ['one', 'two', 'one'],
                    'lval': [1, 2, 3]})

# print(df1)

res = pd.merge(df1, df2,left_on="key1",right_on="key3")

print(res)
