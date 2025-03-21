#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score,mean_squared_error,confusion_matrix,root_mean_squared_error
import os
os.chdir("C:\\uhh\\nptel\\python for datascience\\practice\\")

# %%
df = pd.read_csv("ServiceTest.csv")
df.info()
df.describe()
dff=df.copy()
# %%
dff['Service'] = dff['Service'].map({'Yes': 1, 'No': 0})
x = dff.drop('Service', axis=1)
y = dff['Service']
# %%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)
model = LogisticRegression(solver='liblinear')
model.fit(x_train, y_train)
prediction = model.predict(x_test)
con_mat = confusion_matrix(y_test, prediction)
print(con_mat)
true_positive = con_mat[1, 1]
true_negative = con_mat[0, 0]
print(f"True Positive = {true_positive}, True Negative = {true_negative}")
print(len(y_test),len(prediction))
print(accuracy_score(y_test, prediction))
# %%
ghi = pd.read_csv("GHI_Report.csv")
ghi.info()

# %%
x = ghi[['Economy', 'Fam', 'Health', 'Freedom']]
y = ghi['H_Score']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=1)
model = LinearRegression()
model.fit(x_train, y_train)
prediction = model.predict(x_test)
rmse = np.sqrt(mean_squared_error(y_test, prediction))
print(rmse)

# %%
