#%%
import pandas as pd
import os
import numpy as np
os.chdir("C:\\uhh\\nptel\\python for datascience\\w03")
# Missing Values Present in the Data
cars_data1 = pd.read_csv('ToyotaCleaned.csv',index_col=0)
# if-then-else
# if-then-elif-else
# while-then do-while-then for-loop

# create 3 bins from price var using if else and for loop
# binned values stored as class in new column
cars_data1.insert(10, 'Price_Class', '')
for i in range (0,len(cars_data1['Price']),1):
    if(cars_data1['Price'][i] <= 8450):
        cars_data1['Price_Class'][i] = 'Low'
    elif(cars_data1['Price'][i] > 11950):
        cars_data1['Price_Class'][i] = 'High'
    else:
        cars_data1['Price_Class'][i] = 'Medium'

# Check Frequency of each class
# Syntax: Series.value_counts()
print("Frequency of each class:\n", cars_data1['Price_Class'].value_counts())

# Function in Python
# Syntax: def function_name(parameters):

# Convert Age variable from months to years
# Syntax: DataFrame.apply(lambda x: x/12)
# cars_data1['Age'] = cars_data1['Age'].apply(lambda x: x/12)
# using python function it can be done as

cars_data1.insert(11,'KM_per_Month','0')
# Function with multiple inputs and outputs
def c_convert(val1,val2):
    val1_conv = val1/12
    ratio = val2/val1
    return [val1_conv,ratio]
cars_data1['Age_Years'],cars_data1['KM_per_Month'] = c_convert(cars_data1['Age'],cars_data1['KM'])

# %%
cars_data1.insert(11, 'Age_Years', '0')
def age_conv(val):
    val_conv = val/12
    return val_conv
cars_data1['Age_Years'] = age_conv(cars_data1['Age'])
cars_data1['Age_Years'] = round(cars_data1['Age_Years'],1)



# %% 
i=0
while i<len(cars_data1['Price']):
    if(cars_data1['Price'][i] <= 8450):
        cars_data1['Price_Class'][i] = 'Low'
    elif(cars_data1['Price'][i] > 11950):
        cars_data1['Price_Class'][i] = 'High'
    else:
        cars_data1['Price_Class'][i] = 'Medium'
    i = i + 1

#according to pandas 3.0

cars_data1['Price_Class'] = pd.cut(cars_data1['Price'], bins=[-np.inf, 8450, 11950, np.inf], labels=['Low', 'Medium', 'High'])



# %%
