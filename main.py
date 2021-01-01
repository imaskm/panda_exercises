import pandas as pd

# data = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
#         "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
#         "area": [8.516, 17.10, 3.286, 9.597, 1.221],
#         "population": [200.4, 143.5, 1252, 1357, 52.98]}
#
# b = pd.DataFrame(data)
# b.index = ["BR", "RU", "IN", "CH", "SA"]
#
# print(b)

df1 = pd.DataFrame({'employee': ['Emma', 'George', 'Lisa', 'Olivia'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Emma', 'Olivia', 'Jacob', 'George', 'Lisa'],
                    'hire_date': [2004, 2008, 2012, 2014, 2009]})

res = pd.merge(df1, df2, how='outer')

print(res)
#
# # Program to create Dataframe of three series
# import pandas as pd
#
# # Define series 1
# s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])
#
# # Define series 2
# s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3])
#
# # Define series 3
# s3 = pd.Series(['a', 'b', 'c', 'd', 'e'], ["j", "k", "l", "m", "n"])
#
# # Define Data
# Data = {'first': s1, 'second': s2, 'third': s3}
#
# # Create DataFrame
# dfseries = pd.DataFrame(Data)
#
# print(dfseries)
