'''
"исходный код"
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''

# перевод исходного кода в one hot вид без get_dummies.
import pandas as pd
import random

# Генерируем исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразуем в one-hot вид
one_hot_data = pd.DataFrame()
for category in data['whoAmI'].unique():
    one_hot_data[category] = (data['whoAmI'] == category).astype(int)

# Печатаем первые несколько строк
print(one_hot_data.head())