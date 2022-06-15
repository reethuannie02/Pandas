#Basic method
import pandas as pd
data = {'Name':['Princy','Jai','Anirudh','Sano'],
        'Age' : [27,25,30,22],
        'Address' : ['Delhi','Kochi','Mumbai','Varanasi'],
        'Qualification' : ['M.sc', 'MA','MCA','PhD']
        }
df = pd.DataFrame(data)
print(df)
print(df[['Name','Address']])
print(df[df.columns[0:2]])

#using loc
print(df.loc[1:3,'Age':'Qualification'])
print(df.loc[2,'Name':'Qualification'])

#using .iloc
print(df.iloc[0:2,0:3])
print(df.iloc[2])













