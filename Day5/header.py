import pandas as pd

data = {'Name' : ['Ankith', 'Athul', 'Akshath', 'Adith', 'Ayana', 'Elsa'],
        'Ages' : [21, 23, 20, 20, 23, 20] 
        }

df = pd.DataFrame(data)
print(df.head())
print(df.head(3))