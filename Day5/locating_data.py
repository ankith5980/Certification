import pandas as pd

data = {
    'Name' : ['Ankith', 'Athul', 'Akshath', 'Adith', 'Ayana', 'Elsa'],
    'Ages' : [21, 23, 20, 20, None, 20],
    'Scores' : [98.7, 98.0, 98.0, 96.9, 97.4, 98.5]
}

df = pd.DataFrame(data, index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(df.loc['a'])
print(df.loc['b', 'Name'])
print(df.loc[:, ['Name']])
df.iloc[0,1]