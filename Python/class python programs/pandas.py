# import pandas package
import pandas as pd
 
# list of strings
lst = ['the',"second",'class']
 
# Calling DataFrame to make the list a dataframe
# the columne name is by default 0, and the row names are by default some serial number
df = pd.DataFrame(lst)
print(df) 

# arrange a list of list to a dataframe
## each element of the list will be a record in the dataframe
data = [[2, 3, 4, 5],
        [20, 21, 19, 18]] 
df=pd.DataFrame(data)
print(df)

# renaming columns of data frame
df.columns=['a','b','c','d']
print(df) 

# we can also directly name the columns when the data frame is created using columns=['a', 'b', 'c','d'])
data2 = [[2, 3, 4, 5],
        [20, 21, 19, 18]] 
df=pd.DataFrame(data2, columns=['x','y','z','a'])
print(df)

# arrange dictionary into a dataframe
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]} # the column names are already included.
df = pd.DataFrame(data)
print(df)

'''
Using the pd.DataFrame method, create a DataFrame from a dictionary 
that contains information about cars, such as brand, price, and horsepower.

'''
cars = {'brand': ['Honda', 'Benz', 'BMW', 'Audi'],
        'price': [25000, 36000, 40000, 60000],
        'horsepower': [300, 429, 300, 450]}
df = pd.DataFrame(cars)
print(df)

# change row index
df.rename(index={0: 'Row_1',1:'Row_2',2:'Row_3'}, inplace=True)
print(df)

# arrange np array into a dataframe
import numpy as np
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
print(df)

# setting index
students = [['jack', 34, 'Sydeny', 'Australia',85.96,400],
            ['Riti', 30, 'Delhi', 'India',95.20,750],
            ['Vansh', 31, 'Delhi', 'India',85.25,101],
            ]
df = pd.DataFrame(students)
print(df)
df.columns=['Name', 'Age', 'City', 'Country','Agg_Marks','ID'] # set column name
print(df)
df.set_index("Name",inplace=True) # set index/Row labels
print(df)
df.reset_index(drop=False, inplace=True) # reset index
print(df)

#-----------------------------------------------------------
# create dataframe from csv files
import os
os. getcwd()
os.chdir(r'/Users/sindhujaarivukkarasu/Documents/BAN 601 Tech Fund/class python programs') # please find your directory accordingly 

df = pd.read_csv("nba.csv", index_col ="Name") # you need to specify a column as index in order to extract records by that index
# but in this example, we will use the default index -> a series of integers
df = pd.read_csv("nba.csv")
print(df)

#-----------------------------------------------------------
# column slicing
print(df[["Name","Team"]]) # get multiple columns as another dataframe
print(df["Name"]) # get a data series
print(df[["Name"]]) # get a dataframe

# in order to do row slicing and row/col slicing, we need to use loc and iloc method
# get a particular atomic value
print(df.loc[0,"Name"])
print(df.iloc[0,0])
# get a single row as data series
print(df.loc[0,:])
print(df.iloc[0,:])
# get a single row as dataframe
print(df.loc[[0],:])
print(df.iloc[[0],:])

# get a single column as data series
print(df.loc[:,"Name"])
print(df.iloc[:,0])
# get a single column as dataframe
print(df.loc[:,["Name"]])
print(df.iloc[:,[0]])

# get multiple rows and multiple columns as dataframe
print(df.loc[0:3,["Name","Team"]]) # a range of rows + some specific columns
print(df.iloc[0:3,[0,1,4]]) # a range of rows + some specific columns
print(df.loc[[1,2,5],["Name","Team"]]) # some specific rows + some specific columns
print(df.iloc[[1,2,5],[0,1,4]]) # some specific rows + some specific columns

# we cannot do a range of columns using loc, since loc only take column names to do column slicing
# we can only do a range of columns using iloc, since iloc can do column slicing using column indexes
print(df.iloc[1:4,3:6])


# some commonality between dataseries and a one-dim dataframe 
data_series = df.loc[:,"Age"]
data_frame = df.loc[:,["Age"]]
# length of the data array
print(len(data_series))
print(len(data_frame))
# iteration
for i in data_series:
    print(i)
for i in data_frame: # in data frame, column is recognized before rows. 
    print(i)

# some difference between data series and a one-dim dataframe
# extract a single value
#print(data_series.loc[2])
print(data_series.iloc[2]) # an atomic int, can be used directly in calculation
#print(data_frame.loc[2]) 
print(data_frame.iloc[2]) # a data series, can not be used directly in string operation
print(data_series[len(data_series)-1]) # the last element in the data_series, but we cannot use data_series[-1].
print(data_frame.iloc[-1]) 

# slicing
print(type(data_series.iloc[:2])) # get a data series
print(type(data_frame.iloc[:2])) # get a data frame

#-----------------------------------------------------------
'''
Slicing DataFrames:
Extract only the brand and price of the cars from the cars DataFrame.
'''
cars = {'brand': ['Honda', 'Benz', 'BMW', 'Audi'],
        'price': [25000, 36000, 40000, 60000],
        'horsepower': [300, 429, 300, 450]}
cardf = pd.DataFrame(cars)
print(cardf)

x=cardf.loc[:,["brand","price"]]
print(x)
print(type(x))

#-----------------------------------------------------------

# where is the largest/smallest value
print(data_series.argmax())
print(data_series.argmin())
print(data_frame.argmax()) # data frame cannot do argmax argmin
print(data_frame.argmin())
print(data_frame.min())
print(data_frame.max())

#pls check: max() & min () same for both:

print(data_series.max())
print(data_series.min())

print(data_frame.max())
print(data_frame.min())    
    
#location of max and min values:
#argmax, argmin & idxmax, idxmin for data series:

print(data_series.argmax())
print(data_series.argmin())

print(data_series.idxmax())
print(data_series.idxmin())  

#location of max and min values: idxmax, idxmin for data frame:
    
print(data_frame.idxmax())
print(data_frame.idxmin())     

print(data_frame.argmax()) #not supported for dataframe
print(data_frame.argmin()) #not supported for dataframe

#-----------------------------------------------------------    
    
# sorting
data_series.sort_values()
data_frame.sort_values(by="Age")

# you will find more differences when working with these data objects
# data frame logical slicing
# let's keep using the nba.csv file

condition = df["Age"]>=0 #output: dataseries
condition1 = df[["Age"]]>=0 #own try output: dataframe

# get a bunch of true/false
# let's get the rows with age greater than 25
df2 = df.loc[df["Age"]>=25,:]
df2 = df.iloc[df["Age"]>=25,:] # cannot do this using iloc, logical indexing is only available using loc

# get the rows with age greater than 25 and weight smaller than 180
df3 = df.loc[(df["Age"]>=25) & (df["Weight"]<200),:] # in data frame we have to use & instead of and, | instead of or, ~ instead of not

# get the rows with position equal to PG or SG
posLst = ["PG","SG"]
df4 = df.loc[df["Position"].isin(posLst),:]

# get the rows with position not equal to PG or SG
df5 = df.loc[~df["Position"].isin(posLst),:]

# since the meaning of & and | can be overriden in the class, therefore pandas uses & | ~
# however, and and or are standard operators and their behavior is not overridable

'''From the nba.csv file, extract records of players who play for the 'Golden State Warriors' and have a salary above 5 million.
'''
df6 = df.loc[(df["Team"]=='Golden State Warriors') & (df["Salary"]>5000000),:]
print(df6)

#-----------------------------------------------------------

# add calculated column
df["MonthlySalary"] = df["Salary"]/12
df["Weight2salary"] = df["Weight"]/df["Salary"]

# we need to use np.where when the calculated column is a binary value depending on the other columns
# np.where
a = np.arange(9).reshape((3, 3))
print(a)
print(np.where(a < 4, -1, 100)) # replace values lower than 4 with -1, otherwise replace with 100

# because data series allows for elementwise calculation (check out print(df['Age']<25)), 
print(df['Age']<25)

# np.where can also be used on data series
print(np.where(df['Age']<25,"Young","Old")) # get the age column but replace ages lower than 25 with "Young" and ages higher than 25 with "Old"

# use np.where for binary calculated column
# add one column called "Young", which assign the value "Young" if the age is below 25, and "Old" otherwise.
df["Young"] = np.where(df["Age"]<25,"Young","Old")

# add one column called "success", which assigns 1 if the salary/age is greater than 10**5, and 0 otherwise
df["Success"] = np.where(df["Salary"]/df["Age"]>=10**5, 1, 0)


# multi-valued calculated column
# add one column called "SalaryCategory", which assigns 0 if salary is above 6 * 10 ** 6, 
# 1 if salary is between 3 * 10 ** 6 to 6 * 10 ** 6, 
# and 2 if salary is below 3 * 10 ** 6
# we need to create our own element wise (i.e., row by row) calculation function
def cat(row):
    '''
	takes a row dataseries and return an integer
	'''
    if row['Salary'] < 3 * 10 ** 6:
        res = 2 
    elif row['Salary'] < 6 * 10 ** 6:
        res = 1
    else:
        res = 0
    return res

# apply function cat to each row (axis = 1 or "columns", iterate the column), 
# for each row, the cat function will calculate a value
# lastly, these calculated values are assigned to a column "SalaryCategory"
# apply cat function to each row and returns a data.series object
df['SalaryCategory'] = df.apply(cat, axis=1) 

#--------------------------------------------------------------

# table joins

df1 = pd.DataFrame({'StuID': ['1', '2', '3', '4', '5'],
                   'gender': ['F', 'F', 'M', 'M', 'F']})
print(df1)
df2 = pd.DataFrame({'StuID': ['1', '2', '4','6','7'],
                   'score': [90, 87, 67, 77, 87]})

print(df2)

# concatenate
# putting one dataframe under another one, missing values will be replaced with NaN
df3=pd.concat([df1,df2],sort=False) 
print(df3)

# inner join, only join when there is common ID in two tables
df4=pd.merge(df1, df2, on='StuID',how='inner')
print(df4)

# outter join, use all ID we can find, fill NAN for missing values
df5=pd.merge(df1, df2, on='StuID', how='outer')
print(df5)

# right outter join, keep all ID from the right table, fill NAN for missing values
df6=pd.merge(df1, df2, on='StuID', how='right')
print(df6)

# left outter join, keep all ID from the left table, fill NAN for missing values
df7=pd.merge(df1, df2, on='StuID', how='left')
print(df7)

'''
Create two DataFrames: one containing student names and their student IDs,
and another one containing student IDs and their respective scores in a test. 
Join these DataFrames on student ID.
'''
students = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'StuID': [101, 102, 103]
})

scores = pd.DataFrame({
    'StuID': [101, 102, 103],
    'Score': [90, 85, 88]
})
new=pd.merge(students,scores,on='StuID')
print(new)

#--------------------------------------------------------------

# dataframe grouping

df = pd.read_csv("nba.csv") # you need to specify a column as index in order to extract records by that index
group1 = df.groupby("Team")
#print(group1)
df_mean = group1.mean() # get the mean values for all numeric column
                            # columns that contain non-numeric numbers are omitted
                            # the reuslt itself is a dataframe
df_mean = df.groupby('Team', as_index=False).mean() # without the index, columns that cannot accept mean operation will use the first value in that group.
df_max = df.groupby('Team', as_index=False).max()
df_min = df.groupby('Team', as_index=False).min()
df_sum = df.groupby('Team', as_index=False).sum()

#--------------------------------------------------------------------------------------------

# define custom function to apply to each group

import statistics

def weightstdev(df):
    return statistics.stdev(df["Salary"])

def totalsalary2totalweight(df):
    return df["Salary"].sum()/df["Weight"].sum()

def sumofsquared(df):
    df["square_salary"]=df["Salary"]**2 # first calculate a column
    return df['square_salary'].sum()

df_salarystdev = df.groupby("Team",as_index=False).apply(weightstdev)
df_salary2weight = df.groupby("Team",as_index=False).apply(totalsalary2totalweight)
df_sumofsquaredsalary = df.groupby("Team",as_index=False).apply(sumofsquared)

df_salarystdev = df.groupby("Team",as_index=True).apply(weightstdev).reset_index(name='your_col_name')

'''
From the nba.csv file, find the average age of players for each team.
'''
df = pd.read_csv("nba.csv")
print(df)

def playersAvgage(df):
    return statistics.mean(df["Age"])

df_players = df.groupby("Team",as_index=False).apply(playersAvgage)

#simple method: directly using mean function from pandas
df_players1 = df.groupby("Team",as_index=False)["Age"].mean()


'''
dataframe grouping exercise
generate one column called "MostSuccessfulAtAge", which assigns a value 1 
if the player has the highest salary among his same-aged peers
df = pd.read_csv("nba.csv")

step1, get the highest salary per age using groupby 
step2, merge df_highestsalaryatage into df
step3 (not necessary), change name of the new column from None to "HighestSalaryAtAge" 
step4, calculate the binary variable
'''
df = pd.read_csv("nba.csv")
print(df)

df_highestsalaryatage = df.groupby("Age",as_index=False)["Salary"].max()
print(df_highestsalaryatage)

df_highestsalaryatage.rename(columns={"Salary": "HighestSalaryAtAge"}, inplace=True)
print(df_highestsalaryatage)

df = pd.merge(df, df_highestsalaryatage, on="Age", how="left")
print(df)

df["MostSuccessfulAtAge"]=np.where(df['Salary']== df['HighestSalaryAtAge'],"1","0")
print(df)

#---------------------------------------------------------------------------------------------




