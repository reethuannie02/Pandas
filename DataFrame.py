# Creating DF using single list or list of lists
import pandas as pd
l = ['geeks','for','geeks','is','portal','for','geeks']
series = pd.Series(l)
print(series)

df = pd.DataFrame(l)
print(df)

df = pd.DataFrame(l, columns = ['string'])
print(df)

#Creating DF from dict of narrays/lists:

x = pd.DataFrame({"Name":['Bob','Sam','Anne'],"Marks":[76,25,92]})
print(x)
print(type(x))

#creating an empty dataframe
df = pd.DataFrame()
print(df)

#creating Df from lists of list
import pandas as pd
data = [['tom',10],['nick',15],['juli',14]]
df = pd.DataFrame(data, columns = ['Name','Age'])
print(df)

#Creates a indexes DF using arrays
data = {'Names':['Tom','Jack','Nick','July'],'Marks':[99,98,95,90]}
df = pd.DataFrame(data, index =['rank 1','rank 2','rank 3','rank 4'])
print(df)

#creating df from list of dict
import pandas as pd
data = [{'a':1,'b':2,'c':3},{'a':10,'b':20,'c':30}]
df = pd.DataFrame(data)
print(df)

##creating DF using zip function (#two lists can be merged using list(zip()) fn)
import pandas as pd
Name = ['Tom','Krish','Nick','July']
Age = [25,30,26,22]
list_of_tuples = list(zip(Name, Age))
list_of_tuples
df = pd.DataFrame(list_of_tuples, columns =['Name','Age'])
print(df)