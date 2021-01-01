import pandas as pd
grad = {'2015-16': {'Male': 7980, 'Female': 12490},
        '2016-17': {'Male': 8090, 'Female': 13075},
        '2017-18': {'Male': 8410, 'Female': None}}

df_grad = pd.DataFrame(grad)

# print(df_grad)

df_grad.loc["Female", '2017-18'] = 13895

# print(df_grad)

df_grad_new = df_grad.T

df_grad_new["Total"] = df_grad_new["Male"] + df_grad_new["Female"]
print(df_grad_new)

print(df_grad_new["Total"])

# res =
print('2014-15' in df_grad_new.index )

