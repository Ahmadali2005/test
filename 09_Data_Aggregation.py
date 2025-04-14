#The data must be available or converted to a dataframe to apply the aggregation functions.


# Pandas dataframe.rolling() function provides the feature of rolling window calculations. 
# In very simple words we take a window size of k at a time and perform some 
# desired mathematical operation on it. A window of size k means k consecutive values at a time. 
# In a very simple case, all the ‘k’ values are equally weighted.

# window : Size of the moving window. This is the number of observations used for calculating the statistic. Each window will be a fixed size. 
# If its an offset then this will be the time period of each window. Each window will be a variable sized based on the observations 
# included in the time-period. This is only valid for datetimelike indexes. 
# min_periods : Minimum number of observations in window required to have a value (otherwise result is NA). For a window that is 
# specified by an offset, this will default to 1. 
#freq: "S", "30S", "M" , "30min", "H", "2H"
# import pandas 
import pandas as pd
import numpy as np
import random
# create dates in the range with 12 and Hours
data= pd.date_range('1/1/2024', periods = 12, freq ='1y')

# create dataframe- date column for the date data
data = pd.DataFrame(data,columns=['date'])

##add values column to the dataframe
data['values']=[23,45,32,4,55,44,34,34,67,89,55,34]

# f = np.random.normal(50,5,100)
# print(f.std())
# display
print(data)
#
#print("===========rolling(2).mean()======================")
# print(data['values'].rolling(8, min_periods=5, step=1).max())
###
#print("===========rolling(5).mean()======================")
#print(data['values'].rolling(1).mean())
#
#print("===========rolling(2).min()======================")
#print(data['values'].rolling(2).min())
#
#print("===========rolling(5).min()======================")
#print(data['values'].rolling(5).min())
#
#print("===========rolling(2).max()======================")
#print(data['values'].rolling(4).max())
#
#print("===========rolling(7).max()======================")
#print(data['values'].rolling(7).max())
#
#print("===========rolling(2).sum()======================")
# print(data['values'].rolling(12).sum())
#
#print("===========rolling(45).sum()======================")
#print(data['values'].rolling(2).std())
#

x =  [random.randint(1,100) for i in range(1,100)] 
# print(random.sample(range(1,100), 10))
# print(x)
# print(np.random.random_integers(1,100,5))

df = pd.DataFrame(np.random.randn(10, 4), 
      index = pd.date_range('1/1/2000', periods=10), 
      columns = ['A', 'B', 'C', 'D']) 

#print("===========Data Frame 2 ======================") 
print (df) 
#
#print("===========Apply Aggregation on a Single Column of a Dataframe======================")
##
print (df['A'].rolling(4).aggregate(np.sum) )
#print (df['A'].rolling(4).sum())
##
print (df[['A', 'B']].rolling(4).sum())