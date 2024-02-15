#pandas
#Pandas is usually imported under the pd alias.

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

mydf = pd.DataFrame(mydataset)
print(mydf)

#The version string is stored under __version__ attribute.
print(pd.__version__)

#Series = A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

#Labels - If nothing else is specified, the values are labeled with their index number. 
#First value has index 0, second value has index 1 etc.
#This label can be used to access a specified value.

print(myvar[0])

#Create Labels
#With the index argument, you can name your own labels.

a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

print(myvar["y"])

#Key/Value Objects as Series
#You can also use a key/value object, like a dictionary, when creating a Series.

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

#Note: The keys of the dictionary become the labels.

#To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

#DataFrames:
#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
#Series is like a column, a DataFrame is the whole table.

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)

#Locate Row:
#the DataFrame is like a table with rows and columns.
#Pandas use the loc attribute to return one or more specified row(s)

print(df.loc[0])

#Note: This example returns a Pandas Series.

#Note: When using [], the result is a Pandas DataFrame.

print(df.loc[[0, 1]])

#Named Indexes
#With the index argument, you can name your own indexes.

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

#Locate Named Indexes
#Use the named index in the loc attribute to return the specified row(s).

print(df.loc["day2"])

#Load Files Into a DataFrame
#If your data sets are stored in a file, Pandas can load them into a DataFrame.

import os
os. getcwd()
os.chdir(r'/Users/sindhujaarivukkarasu/Documents/BAN 601 Tech Fund/class python programs') # please find your directory accordingly 

df = pd.read_csv('nba.csv')
print(df) 

#Viewing the Data - The head() method returns the headers and a specified number of rows, starting from the top.

df = pd.read_csv('nba.csv')
print(df.head(10))

#The tail() method returns the headers and a specified number of rows, starting from the bottom.

print(df.tail()) 

