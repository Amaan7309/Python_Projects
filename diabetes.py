import numpy as np
import pandas as pd
import matplotlib as plt

df = pd.read_csv('diabetes.csv')
# print(df.head())

#Returns all the rows and columns
# print(df.shape)

# Gives both head and tail
# print(df.describe)

#Shows stats like mean median quartile etc.
# print(df.describe())

# Printing all the columns
columns = list(df)
# print(columns)

#Checking If there is a null value
# print(df.isnull().sum())

# Checking all the 0's which are error values
# print((df[columns[1:6]] == 0).sum())

# Replacing 0 with Nan
df[columns[1:6]] = df[columns[1:6]].replace(0,np.nan)
# print(df.describe)

# Now the null values came as we have added them as NaN
# print(df.isnull().sum())

# This guy of Unified Mentor tells to delete the data null values when there is more than 45% or more than it.
df = df.dropna()
print(df.describe)

