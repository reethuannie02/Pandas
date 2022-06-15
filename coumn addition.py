
import pandas as pd
data = {'Name': ['Princy','Sai','Jason','Aby'],
        'Height' : [5.1,4.9,5.4,6.1],
        'Qualification': ['M.Sc','MCA','Engg','Phd']
         }
df = pd.DataFrame(data)
address = ['Kochi','Delhi','Chennai','Puna']
df['Address'] = address
print(df)

#using insert
df.insert(1,'Age',[24,20,26,31])
print(df)

#using assign
import pandas as pd
data = {'Name': ['Princy','Sai','Jason','Aby'],
        'Height' : [5.1,4.9,5.4,6.1],
        'Qualification': ['M.Sc','MCA','Engg','Phd']
         }
df = pd.DataFrame(data)
df1 = df.assign(Marks = [26,28,20,13])
print(df1)




