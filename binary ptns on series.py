import pandas as pd
l1 = [10,20,30,40,50,60,70,80,90]
l2 = [1,2,3,4,5,6,7,8,9]
s1 = pd.Series(l1)
s2 = pd.Series(l2)
print(s1.add(s2))
print(s1.sub(s2,fill_value = 0))

x1 = [10,20,30,40]
x2 = [9,5,3,2]
s3 = pd.Series(x1, index = ['a','b','c','d'])
s4 = pd.Series(x2, index = ['c','b','e','f'])
print(s3)
print(s4)
print(s3.add(s4)) #both having same indexes are added n rest r shown as Nan
print(s3.add(s4,fill_value = 0)) # all indexs are added n not matching ones are considered as zero
print(s3.mul(s4,fill_value = 1))