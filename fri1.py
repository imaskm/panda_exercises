# import pandas as pd
# import numpy as np
#
# df_10 = pd.DataFrame({'customer_id': [3, 2, 9, 4, 5, 8, 10, 1, 15, 11, 6, 7, 12, 14, 13],
#                       'gender': ['M', 'F', 'M', 'M', 'F', 'M', 'F', 'F', 'F', 'F', 'F', 'M', 'M', 'M', 'F'],
#                       'customer_age': [22, 21, 35, 40, 22, 28, 25, 43, 33, 37, 27, 30, 20, 50, 32],
#                       'post_code': [85711, 84623, 88282, 85732, 88200, 42610, 85790, 84600, 84686,
#                                     42699, 88211, 42671, 42677, 85723, 88296],
#                       'occupation': ['engineer', 'librarian', 'lawyer', 'scientist', 'engineer', 'librarian', 'artist',
#                                      'engineer', 'lawyer', 'artist', 'engineer', 'lawyer', 'librarian', 'engineer',
#                                      'scientist']})
#
#
# def myfunc(d1, d2):
#     if str(d2).startswith("88"):
#         return d1 + 5
#     else:
#         return d1
import  pandas as pd
import numpy as np

df_5 = pd.DataFrame({'Quiz1':[78,85,96,80,86,76,90],
                     'Quiz2':[84,94,89,83,86,74,82],
                     'Quiz3':[86,97,96,72,83,67,78],
                     'Student':['John', 'Mike', 'Emma', 'Jess', 'Monica', 'Chris', 'Lucy'],
                     'Group':[1,2,1,2,1,2,1]})
# df_5['diff'] = df_5.

print(df_5)


#
#
# df_10['customer_age'] = df_10.apply(lambda x: myfunc(x.customer_age, x.post_code), axis=1)
#
# print(df_10['customer_age'])
