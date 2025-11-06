import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Expanded_data_with_more_features.csv")
#retrives the values of above/top 5 rows
#print(df.head())

# retrives the mean median mode lowest highest values of the data n the form of percentage
# print(df.describe())

# retrives all the column names,isnull,total rows in a column and their datatype
# print(df.info())

# retrives the number of null  values in the dataset
# print(df.isnull().sum())

#dropping un-named column
df = df.drop("Unnamed: 0",axis = 1)
# print(df.info())

# replaces a particular value
# df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-oct, 5-10")

# printing a particular column 
# print(df['WklyStudyHours'])

# creating a chart to see the amount of males and females in the school
# ax = sns.countplot(data = df,x = "Gender")
# ax.bar_label(ax.containers[0])
# plt.show()

# creating a group to check if the education of the parents affect the marks if the child 
# or not
# gb = df.groupby("ParentEduc").agg({"MathScore" : "mean", "ReadingScore" : "mean", 
# "WritingScore" : "mean"})
# print(gb)

# using heatmaop to see the data with the help of light to dark heat
# sns.heatmap(gb , annot = True)
# plt.show()

# creating a group to check if the marital status of the parents affect the marks if the child 
# or not
# gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore" : "mean", "ReadingScore" : "mean", 
# "WritingScore" : "mean"})
# # print(gb1)
# sns.heatmap(gb1 , annot = True)
# plt.show()

# boxplot is used to show the outlier values of a particular column
# sns.boxplot(data = df,x = "MathScore")
# plt.show()

# sns.boxplot(data = df,x = "ReadingScore")
# plt.show()

# sns.boxplot(data = df,x = "WritingScore")
# plt.show()

# checking all the unique values in the table
# print(df['EthnicGroup'].unique())

# here count function without any parameters returns first and last five rows of the dataset
groupA = df.loc[(df["EthnicGroup"] == "group A")].count()
# while here with parameters returns all the column name with numbers of how many time
# they have used
groupB = df.loc[(df["EthnicGroup"] == "group B")].count()
groupC = df.loc[(df["EthnicGroup"] == "group C")].count()
groupD = df.loc[(df["EthnicGroup"] == "group D")].count()
groupE = df.loc[(df["EthnicGroup"] == "group E")].count()

# mlist = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"]
# ,groupE["EthnicGroup"]] 
# plt.pie(mlist)
# plt.show

# ax = sns.countplot(data = df , x  = "EthnicGroup")
# ax.bar_label(ax.containers[0])
# plt.show()