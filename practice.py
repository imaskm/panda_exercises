import pandas as pd
import numpy as np

customer_data = pd.DataFrame(
    {'customer_id': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15'],
     'gender': ['M', 'F', 'M', 'M', 'F', 'M', 'F', 'F', 'F', 'F', 'F', 'M', 'M', 'M', 'F'],
     'customer_age': ['22', '21', '35', '40', '22', '28', '25', '43', '33', '37', '27', '30', '20', '50', '32'],
     'post_code': ['85711', '84623', '88282', '85732', '88200', '42610', '85790', '84600', '84686', '42699', '88211',
                   '42671',
                   '42677', '85723', '88296'],
     'occupation': ['engineer', 'librarian', 'lawyer', 'scientist', 'engineer', 'librarian', 'artist', 'engineer',
                    'lawyer',
                    'artist', 'engineer', 'lawyer', 'librarian', 'engineer', 'scientist'],
     'salary': ['22000', '23000', '45000', '80000', np.nan, '25000', '30000', np.nan, '60000', '43000', '33000',
                '38000',
                '20000', '70000', '45000']})

customer_data['salary'].fillna(customer_data['salary'].median(), inplace=True)

# print(customer_data['salary'])
customer_data['customer_age'] = customer_data['customer_age'].apply(int)

customer_data2 = customer_data.loc[customer_data['customer_age'] >= 30]
customer_data2.reset_index(inplace=True)
# customer_data2['customer_age'] = customer_data2['customer_age'].apply(int)
# print(customer_data2[customer_data2.astype({'customer_age': 'int32'}).customer_age])

# print(customer_data2)

customer_data2['birth_year'] = 2020 -    customer_data2['customer_age']
print(customer_data2)