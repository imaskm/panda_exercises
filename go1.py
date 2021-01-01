# list_a = [1,32,54,8,9,23,6,98,43,2,7,98]
# list_b = [32,3,1,7,98,6,4,6,43,2,13,4]
# list_c = [21,4,7,58,12,79,13,34,69,12,4,5]
# list_sum = [ list_a[i]+list_b[i]+list_c[i] for i in range(len(list_a))]
# print(list_sum)

# letters = ['A','U','B','C','D','A','B','D','A','D','B','A','B','D','L','A','B','B','A','B']
# # letters_new = [ i for i in letters if i not in ['A', 'B', 'D'] ]
# print(letters_new)

# def factorial(n):
#     if n < 0:
#         raise  AssertionError("Please call the function with a non-negative integer")
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(5))

# int_nums = [2, 3, 5, 6, 8, 9, 11, 12, 15, 18]
# int_nums = list(filter(lambda x: x%2!=0, int_nums))
# print(int_nums)
#
# nums = [1, 3, 5, 6, 8]
# nums = sorted(nums, key= lambda x: abs(x-5))
# print(nums)
import pandas as pd

#
# df_sale = pd.DataFrame(data = {'MANAGER':['Anna', 'Anna', 'Martin', 'Anna', 'Martin', 'Martin', 'Anna', 'Martin'],
#                                'CLIENTS':[2, 7, 5, 5, 4, 5, 8, 5],
#                                'AMOUNT':[80.1, 10.2, 10., 80.3, 70., 100.2, 30., 40.5],
#                                'SALESPERSON':['Ben', 'Andrew',  'Elisa', 'Kat', 'Tom', 'Bet', 'Elenore', 'Steve'],
#                                'ACTIVE':['Y', 'Y', 'N', 'N', 'Y', 'Y', 'N', 'N']},
#                        index = pd.DatetimeIndex(['2020-03-01', '2020-05-01', '2020-03-01', '2020-04-01',
#                                                  '2020-04-01', '2020-05-01', '2020-06-01', '2020-06-01']))
#
# # df_sale["MAN_EMPL_EARNINGS"] = df_sale.loc[df_sale.MANAGER+"-"+df_sale.SALESPERSON+"+"+df_sale.AMOUNT.apply(lambda x: str(x))  ]
#
# df_sale["MAN_EMPL_EARNINGS"] = df_sale["MANAGER"]+ "-" + df_sale["SALESPERSON"]+"+" + df_sale["AMOUNT"].apply(str)
#
# print(df_sale)

# df_sale = pd.DataFrame(data = {'MANAGER':['Anna', 'Anna', 'Martin', 'Anna', 'Martin', 'Martin', 'Anna', 'Martin'],
#                                'CLIENTS':[2, 7, 5, 5, 4, 5, 8, 5],
#                                'AMOUNT':[80.1, 10.2, 10., 80.3, 70., 100.2, 30., 40.5],
#                                'SALESPERSON':['Ben', 'Andrew',  'Elisa', 'Kat', 'Tom', 'Bet', 'Elenore', 'Steve'],
#                                'ACTIVE':['Y', 'Y', 'N', 'N', 'Y', 'Y', 'N', 'N']},
#                        index = pd.DatetimeIndex(['2020-03-01', '2020-05-01', '2020-03-01', '2020-04-01',
#                                                  '2020-04-01', '2020-05-01', '2020-06-01', '2020-06-01']))
#
# df_sale.columns = df_sale.columns.str.lower()
#
# print(df_sale)
# df_sale = pd.DataFrame(data = {'MANAGER':['Anna', 'Anna', 'Martin', 'Anna', 'Martin', 'Martin', 'Anna', 'Martin'],
#                                'CLIENTS':[2, 7, 5, 5, 4, 5, 8, 5],
#                                'AMOUNT':[80.1, 10.2, 10., 80.3, 70., 100.2, 30., 40.5],
#                                'SALESPERSON':['Ben', 'Andrew',  'Elisa', 'Kat', 'Tom', 'Bet', 'Elenore', 'Steve'],
#                                'ACTIVE':['Y', 'Y', 'N', 'N', 'Y', 'Y', 'N', 'N']},
#                        index = pd.DatetimeIndex(['2020-03-01', '2020-05-01', '2020-03-01', '2020-04-01',
#                                                  '2020-04-01', '2020-05-01', '2020-06-01', '2020-06-01']))
#
# total = df_sale["AMOUNT"].sum()
# print(total)
# df_sale.rename(columns={"AMOUNT": "AMOUNT_PERCENTAGE"},inplace=True)
# df_sale["AMOUNT_PERCENTAGE"] = round(df_sale["AMOUNT_PERCENTAGE"]/total,2).apply(str)+"%"
#
# print(df_sale)

df_quiz = pd.DataFrame(data={'NAME': ['Ben', 'Elisa', 'Kat', 'Tom', 'Diego', 'Xiaoming', 'Yun', 'Sofia'],
                             'Quiz_1': [90, 80, 70, 90, 40, 60, 77, 80],
                             'Quiz_2': [80, 64, 30, 80, 60, 42, 90, 43],
                             'Quiz_3': [64, 60, 68, 88, 70, 53, 88, 50],
                             'Quiz_4': [73, 93, 80, 94, 73, 60, 80, 87],
                             'Quiz_5': [68, 64, 55, 77, 61, 93, 54, 63],
                             'Quiz_6': [88, 74, 66, 74, 75, 60, 83, 77]})

# df_quiz["FINAL_GRADE"] = round(
#     sum(sorted([df_quiz["Quiz_2"], df_quiz["Quiz_1"], df_quiz["Quiz_3"], df_quiz["Quiz_4"], df_quiz["Quiz_5"],
#                 df_quiz["Quiz_6"]])[2:]) / 4, 1)

df_quiz["FINAL_GRADE"] = [  round(sum(sorted([ row.Quiz_1, row.Quiz_2, row.Quiz_3, row.Quiz_4, row.Quiz_5, row.Quiz_6 ])[2:])/4,1) for index,row in df_quiz.iterrows() ]
print(df_quiz)
