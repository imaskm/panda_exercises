index = ['a', 'b', 'c', 'd', 'x', 'f', 'g', 'h']

import pandas as pd

s1 = pd.Series(range(8))

s2 = pd.Series(range(7, -1, -1))

# print(s1)
s1.index = index
s2.index = index
# print(s1)
# print(s2)

df = pd.DataFrame({"Obj1": s1, "Obj2":s2},index=index)

df.rename(index={"x":"e"}, inplace=True)
print(df)
# print(df["Obj2"])
print(df.loc['d':'e']['Obj2'])
df.sort_index(ascending=False, inplace=True)

# print(df)
