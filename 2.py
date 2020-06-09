#Created on Tue Jun  9 
#@author: pc
# 1 Importing all necessary libraries
import os 
import pandas as pd
os.chdir('D:\Repo\Learn-Pandas-with-PaareshC')
# 2 Load the data
df=pd.read_csv('mpg.csv')
# 3 Subsetting using multiple conditions
# Suppose I want all cars of europe with mpg=25
from_europe=df['origin']=='europe'
mpg_25=df['mpg']==25
req=df[from_europe & mpg_25]
print(req)
# 3.2 Subsetting using .isin
# Suppose I want cars from europe and japan
req2=df[df['origin'].isin(['europe','japan'])]
print(req2)
# 4 SORTING
# 4.1 sorting using horsepower
req3=df.sort_values('horsepower')
print(req3)
# 4.2 suppose you want horsepower in descending order
req4=df.sort_values('horsepower',ascending=False)
print(req4)
# 4.3 sorting for decending horsepower and ascending mpg 
req5=df.sort_values(["horsepower", "mpg"], ascending=[False,True])
print(req5)

