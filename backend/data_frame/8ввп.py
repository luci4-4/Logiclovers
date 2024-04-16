# -*- coding: utf-8 -*-
"""8ввп.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GWTWcNGs5OGUQpj1-749sHRyZItWczsW
"""

import pandas as pd

df = pd.read_csv('section_8.csv',sep=';')

df.drop(range(0,48))
df.drop(range(2208,17664))
print(df)

df1 = df.set_index('year')
print(df1)

df1=df1.drop(['section','indicator_name','indicator_unit','comment','indicator_code'],axis=1)
print(df1)

df1 = df1.loc[df1['object_level'] != 'федеральный округ']
print(df1)

df1=df1.drop(['object_level'],axis=1)
print(df1)

df1 = df1.loc[df1['indicator_value'] != -99999999.0]
print(df1)

test = "Белгородская область"
df_obl = df1.loc[df1['object_name'] == test]
print(df_obl)

from matplotlib import pyplot as plt

years = list(df_obl.index)
val = list(df_obl['indicator_value'])

plt.bar(years, val)

plt.xlabel('Годы')
plt.ylabel('ВВП в миллионах')
plt.title(f'Гистограмма для {test}')

plt.savefig('график.png')
plt.show()