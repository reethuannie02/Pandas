import pandas as pd
df = pd.DataFrame({'Names':['Braud, Mr Harris','Allen, Mr Henry','Bonnell, Ms Elizabeth'],
                   'Age': [22,35,58],
                   'Sex':['Male','Male','Female']
                   })
print(df)
print(df['Age'])
print(df.max())
print(df['Age'].max())
print(df.describe())
