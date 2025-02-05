#%%
import os     # change working directory
import pandas as pd # work with dataframes

os.chdir("C:\\uhh\\nptel\\python for datascience\\w03")
 
data_csv = pd.read_csv('Iris_data_sample.csv')  # import data
# blank cell read as nan

# remove extra id column by passing index_col=0

data_csv = pd.read_csv('Iris_data_sample.csv',index_col=0)

# replacing junk values to nan ?? ###

data_csv=pd.read_csv('Iris_data_sample.csv',index_col=0,na_values=['??','###'])

# %%
import os     # change working directory
import pandas as pd # work with dataframes

os.chdir("C:\\uhh\\nptel\\python for datascience\\w03")
data_xlsx = pd.read_excel('Iris_data_sample.xlsx',sheet_name='Iris_data')
data_xlsx=pd.read_excel('Iris_data_sample.xlsx',index_col=0,na_values=['??','###'])

#%%
import os     # change working directory
import pandas as pd # work with dataframes

os.chdir("C:\\uhh\\nptel\\python for datascience\\w03")
# data_txt1 = pd.read_table('Iris_data_sample.txt')
# data_txt1=pd.read_table('Iris_data_sample.txt',sep = '\t')
data_txt1=pd.read_table('Iris_data_sample.txt',delimiter= ' ')  # default delemiter is tab represented by \t may use comma blank 
# all may not work cross verification with data neccessary 
# here blank delimeter work
data_txt1=pd.read_table('Iris_data_sample.txt',index_col=0,na_values=['??','###'])

# read txt file with read_csv
data_txt2 = pd.read_csv('Iris_data_sample.txt',delimiter= ' ') 

# %%

