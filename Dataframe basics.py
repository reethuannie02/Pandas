import pandas as pd
#Column deletion
# we use drop() fn
import numpy as np
my_df = pd.DataFrame(np.random.randn(25).reshape(5,5), index=['a','b','c','d','e'], columns = ['c1','c2','c3','c4','c5'])
print(my_df)

print(my_df.drop('b')) #it will create new DF ie it wont make changes to the existing one
print(my_df.drop('c1',axis = 1)) #by default it refers d axis to row,so for column v hav eto specify #axis = 1


