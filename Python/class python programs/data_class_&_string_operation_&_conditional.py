# 0.different types of statement 

# sequential
def function_1(x, y):
    a= x+y
    return a
  
function_1(1, 3)
    
'''Write a function sum_and_multiply(a, b) that returns both the sum 
and the product of two numbers. 
The result should be returned as a tuple (sum, product).'''

def sum_and_multiply(a, b):
    return (a + b, a * b)

sum_and_multiply(4,6)

# repeated 
for i in range(1,10):
    x =0
    x += i
    print(x)


# conditional 
x =2
y =4

if x>y:
    print("x is bigger")
else:
	print("y is bigger than or equal to x")

#----------------------------------------------------------------

# 1. list and tuple

# list is the most common way to store data in python
# defining lists

a=['first','second','third']
b=[1,2,3]
c=[] # this is the empty list
d=['first',2,3.14] # list may contain different value types

# checking the number of elements in lists
b=[1,2,3]
c=[]
print(len(b),len(c)) 

# list indexing and slicing
x=[54,12,32,41,33]
print(x[0]) # the first element
print(x[4])
print(x[1:3]) # the 2nd and the 3rd element (1<=x <3)
print(x[-1]) # the last element in list
print(x[-2]) # the second last element in list
print(x[:3]) # the first three element in list
print(x[-3:]) # the last three element in list
print(x[2:]) # the elements from the third one in list
print(x[:-1]) # the elements before the last one in list
print(x[1:-1]) # the elements before the last one in list

# nested list
x=[[1,2,3],[3,2,1]] # this is a list of two sub-lists
y=x[1][2] # the 3rd element in the 2nd list
z=x[0][1] 
print(y,z)

# repeat list
print([0]*4)
print([1,2,3]*4)

# appending to list
t = ['a', 'b', 'c']
t.append('d') 
print(t) 

# insert to list
t = ['a', 'b', 'c']
t.insert(0,'d') # insert 'd' to the first position of the list 
print(t) 

# extend list
t1 = ['a', 'b', 'c'] 
t2 = ['d', 'e'] 
t1.extend(t2) #or you can do t1+t2
print(t1)
t1+t2

# remove from list
t1 = ['a', 'b', 'c']
t1.remove('a')#remove
t1.pop() #remove the last item
t1=['a','b','c']
t1.pop(1) # remove the position 1 item
print(t1)

# list is mutable, meaning that you can update the element inside it
fruit = ['banana', 'apple', 'quince'] 
fruit[0] = 'pear' # updating the first element to pear 
fruit[-1] = 'orange'  # updating the last element to orange
print(fruit) 

# summary statistics for a list
import statistics 
x=[1,2,3]
print(sum(x))
print(max(x))
print(min(x))
print(statistics.mean(x))
print(statistics.median(x)) 

# zip list
x=[1,2,3]
y=[2,3,4]
for i in zip(x,y):
    print(i) # the output is a tuple
	
# join - from list to string with specified delimiters
x=["1","2","3","4"]
print(" ".join(x)) # use space to join character variables
print(", ".join(x)) # use comma and space to join character variables

str1=" ".join(x)
print(str1)
str2=", ".join(x)
print(str2)

# join can only join string list.
x=[1,2,3,4]
print(" ".join(x))

# itertools on a list
# permuatation
import itertools
print(list(itertools.permutations([1,2,3])))
# pairwise permulatation
print(list(itertools.permutations([1,2,3,4,5],2)))
# permutations does not allow repeated elements
# but product allows
print(list(itertools.product([1,2,3,4,5],repeat=2))) # here we cannot omit the "repeat =" 
                                                     # because the first argument of product can take multiple values.

'''Using sorted() function, write a function second_largest(nums) 
that returns the second largest number in a list of numbers. 
For simplicity, you can assume the list has at least two distinct numbers'''

#function to return the second largest number
def seconnd_largest(nums):
    sorted(nums)
    a=(nums[-2])
    print("\nThe second largest number is:")
    return a

nums=[5,3,1,6,2,7,10]
seconnd_largest(nums)

# tuple
# tuple operates almost the same as list, but it is not mutable, 
# meaning that once a tuple is created, it cannot be changed or updated

# immutable
list1 = ['History', 'Math', 'Physics', 'CompSci']#list is mutable
tuple1=('History', 'Math', 'Physics', 'CompSci')#tuple is immutable, we can not edit a tuple, but we can do others
#try the following
list1[0]='Rocket science'
tuple1[0]='Rocket science'

# advantage of tuple over list
# iteration with tuple is faster, immutablity is safer for some applications,

# multiple value assignment with tuple and list
lst=[24,35]
tup=(24,35)

value1,value2=lst
print(value1,value2)

value3,value4=tup
print(value3,value4)

# value swapping with tuple
x=2;y=3
# cannot do this
y=x;x=y# once y is assigned the value of x, the original y value is lost
print(x,y)

# method 1: use an intermediate variable
x=2;y=3
z=x;x=y;y=z
print(x,y)

# method 2: use tuple
x=2;y=3
x,y=(y,x)
print(x,y) # or simply, x,y=y,x because x,y is treated as a tuple.


# check the type of the object
x=[1,2,3]
y=(1,2,3)
print(type(y)==tuple)
print(type(y) is tuple)
print(type(y)==list)
print(type(y) is list)
print(type(x)==list)
print(type(x) is list)

#--------------------------------------------------------------------------------------
# 2. sets

# sets are another way to store data in python. 
# but sets do not allow duplicated values
# sets are defined with {}, and values are delimited by comma
x={1,2,3,1,2,3}
print(x) # notice that the duplicated 3 is gone

# remove duplicates in lists and tuples
y=[1,2,3,3] # define a list
z=(1,2,3,3) # define a tuple
print(list(set(y))) # after removing duplicates with set, convert back to a list
print(tuple(set(z))) # after removing duplicates with set, convert back to a tuple

# add items to a set
color_set = set() # A new empty set, you cannot define an empty set with x={}. 
                  # Because by default, {} will be treated as an empty dictionary
color_set.add("Red") # add one item
print(color_set)
color_set.update(["Blue", "Green"]) # Add multiple items
print(color_set)

# remove items from sets
language = {'English', 'French', 'German'}
language.remove('German') # 'German' element is removed
language

# create intersection of two sets
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
setz = setx & sety
print(setz)
setzz=setx.intersection(sety)
print(setzz)

listx = ["green", "blue"]
listy = ["blue", "yellow"]
listz = listx & listy
listq = listx + listy
print(listq)

# create union of two sets
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
seta = setx | sety
print(seta)
setb = setx.union(sety)
print(setb)

# the difference between sets
x=[1,2,3]
y=[1,2,4]
xy=list(set(x)-set(y)) # remove from set x the common items in set x and set y
yx=list(set(y)-set(x))
print(xy)
print(yx)

# generate symmetric difference between two sets
setx = set(["apple", "mango"])
sety = set(["orange","mango"])
setc = setx ^ sety # symmetric difference is the combination of two sets minus all common items
print(setc)

# or we can do it manually, note that the prerenthesis is needed 
# because the set operation has lower order than + or - in calculation
manual=(setx | sety) - (setx & sety)
print(manual)

'''3. Three-way Symmetric Difference:

Given three sets:
python
Copy code
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
setC = {5, 6, 7, 8}
First, find the symmetric difference between setA and setB. 
Then, with the resulting set, 
find its symmetric difference with setC. Print the final result.
'''
#symmetric difference
setA={1,2,3,4}
setB={3,4,5,6}
setC={5,6,7,8}
setx=setA^setB
print(setx)
sety=setx^setC
print(sety)

#or
setd=setA^setB^setC

# --------------------------------------------------------------------------------------
# 3. dictionary
dct = {'Name': 'Zara', 'Age': 7}
	
# check the following 
print(dict.keys(dct))
print(dict.values(dct))
print(dict.items(dct))
	
# fill in a dictionary
emptydict={}
emptydict['1st entry']=34
emptydict['2nd entry']=True
emptydict['3rd entry']='text'
print(emptydict)

# get method
dct = {'Name': 'Zara', 'Age': 7}
print(dct.get("Name",0))
print(dct.get("Height",0))

# the update method
dct = {'Name': 'Zara', 'Age': 7}
dct_update={'Age':8,'Height':6}
dct.update(dct_update)
dct.update({'Age':8,'Height':6})
print(dct)
dct.update({'Age':9})
print(dct)

# dict.fromkeys
keys=["red","green","white","red"]
print(dict.fromkeys(keys))

keys=["length","breadth","height"]
rectangle=dict.fromkeys(keys,5)
print(rectangle)

# we can remove duplicate and keep the original sequence by using dict.fromkeys
# anything can be the key of a dictionary

# --------------------------------------------------------------------------------------
# 4. string operation

# slicing strings, similiar to lists, sets, tuples.
fruit='banana'
print(fruit[0]) # the first letter in variable fruit
print(fruit[1]) # the second letter in variable fruit
print(fruit[0:2]) # the first two letters in variable fruit
print(fruit[:3]) # up to the first 3 letters in variable fruit
print(fruit[-1]) # the last letter in variable fruit
print(fruit[-3:]) # the 3rd from the last letter to the end.

# Given any string, make the first letter upper case, and the rest lower case. 
def format_string(x):
    string=x[0].upper()
    for i in x[1:]:
        #string+=i.lower()
        #print(string)
        string=string+i.lower()
    return string
print(format_string('sINDhu'))

# checking if a substring is in a string
word='banana'
print('nana' in word) # 'nana' is in 'banana', True
print('ana' in word) # 'ana' is in 'banana',.True
print('c' in word) # 'c' is not in 'banana' False

# check the number of appearance of substring
word="banana"
print(word.count('na'))

# locating the position of substring in a string
word='banana'
index=word.find('na') # find the index of 'na' inside 'banana', the starting index of 'na' is 2.
print(index)
nonexistence_index=word.find('c') # if the string cannot be found, the returned index is set to -1
print(nonexistence_index)

# replacing substrings
x='banana'
y=x.replace('na','') # replace 'na' inside 'banana' with empty string
print(y)
z=x.replace('na','z') # replace 'na' inside 'banana' with 'z'
print(z)

# replace multiple charaters at the same time
symbollist=''''"!@#$%^&*()+~[]{}''' # when a string has both single quote and double quote, you have quote it with triple quote.
# this is how multiple replace is done
symboldict=dict.fromkeys(symbollist,"_")
t=str.maketrans(symboldict) # this converts the symboldict into another dictionary
                            # where the keys are the ascii code for each symbol.
text1="I can't do it"
text2="email is xy@csueb.edu"
print(text1.translate(t))
print(text2.translate(t))

# find all words in a list that starts with letter c
x=['California','State','University','East','Bay','is','committed','to','being','a','safe','and','caring','community']
count=0
for i in x:
    lowercase=i.lower() # convert everything lowercase
    if lowercase.startswith('c'): # check if the converted string starts with 'c', the startswith is case sensitive
        print(i)
        count=count+1
print(count)

# replace phrase "not ...... poor " with 'good', such as 'not that poor' or 'not very poor'
def not_poor(string):
    index_not=string.find('not') # check the position of 'not'
    print(index_not)
    index_poor=string.find('poor') # check the position of 'poor'x=['California','State','University','East','Bay','is','committed','to','being','a','safe','and','caring','community']
    print(index_poor)
    if index_not > 0 and index_poor > 0 and index_not < index_poor: # if both index is greater than 0, and 'not' is before 'poor'
        tobereplaced=string[index_not:(index_poor+4)] # then we are going to replace this string, we add 4 to the index_poor since poor itself has 4 letters
        returnstring=string.replace(tobereplaced,'good') # replace 'not'......'poor'  with 'good'
        return returnstring
    else:
        return string
print(not_poor('The lyrics is not that poor!'))

'''"
I am not that poor"
5:14+4
'''

# Write a Python program to get a string from a given string where all occurrences of
# its first char have been changed to '$', except the first char itself
# for example, the word 'restart' will be changed to 'resta$t'

def change_char(str1):
    a=str1[0] 
    str1=str1.replace('r','$')   
    str1=a+str1[1:]
    print("\nThe Modified string is:")
    return str1  
print(change_char('restart'))

print(change_string('er'))
print(change_string('eree'))
print(change_string('ereeing'))

def find_string():
    pass

# --------------------------------------------------------------------------------------
# 5. string formatting

print('%s->%d;' % ('cat', 3)) # %s is a placeholder for a string %d = intger number
print('%s->%d;' % 'cat') #missing argument error
print('%d' % 3)
	
print('%d' % 4.5)# remember %d is an integer number
print('%f' % 1.234) # float number, but with 6 digits by default
print('%.2f' % 1.234) # check out the outputs
print('%.3f' % 1.234) # check out the outputs
print('%.4f' % 1.234) # check out the outputs

count=2312
total = 128310
template='accuracy for %d words:%.3f%%' 
#the percent character % has a special interpretation in formatting strings, have to precede it with another % to output.
print(template % (total, count))

# format the strings using the format function
print("I have {} balloons.".format(5))
print("The {} has a pet {}!".format("shark", "pilot fish"))
print("The {0} has a pet {1}!".format("shark", "pilot fish"))
print("The {1} has a pet {0}!".format("shark", "pilot fish"))
print("Sally is a {3}, {2}, and {1} {0}!".format("happy", "smiling", "blue", "shark"))

'''Using:
values = [3, "cats", "dogs"]
Print: "I have 3 pets: 2 cats and 1 dog." (Hint: Mix positional formatting and hardcoding some values.)

'''
print("I have {} pets: {} cats and {} dog.".format(3,2,1))
print("I have {0} pets: {1} cats and {2} dog.".format(3,2,1))

# you can use dictionary, too. 
person = {"name": "John", "age": 30}
print("{name} is {age} years old.".format(**person))

# here is a simpler way for .format method.
x=2
y=2.2
print(f"x is {x}, and y is {y}")
print(f"x squared is {x**x}, and the integer part of y is {int(y)}")

# --------------------------------------------------------------------------------------
# 6. conditional statement

# basic structure of conditional statement
x=5
if x > 0:
    print('x is positive')
	
# the else statement
x=-5
if x > 0:
    print('x is positive')
else:
    print('x is negative')

# check if a number is even or odd
x=6
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')

# when there are more than 2 options
x=6
if x == 0:
    print('zero')
elif x%2 == 0:
    print('even')
else:
    print('odd')

# nested if statement
x=6
if type(x)==int: # only move forward when the input number is integer
    if x>10:
        x=x+1
    else:
        x=x-1
    print(x)
else:
    print('not an integer')

# inline if statement
y = 0
x = 5
z  =  x/y  if y != 0 else 'division by zero'
print(z)

# determine the letter grade based on the grand total
score = 85
if score >=90:
    print("A")
elif score >=70:
    print("B")
elif score >=80:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")
# it is important to know that the sequence of
# the if statement matters since it checkz sequentially.

# concatenated conditions
midscore = 90
finalscore = 90
if midscore >=90 and finalscore >=90:
    print("super")
elif midscore >=90 or finalscore >=90:
    print("OK")
else:
    print("Poor")

# print number of days given a month
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
	print("No. of days: 28/29 days")
elif month_name in ["April", "June", "September", "November"]:
	print("No. of days: 30 days")
elif month_name in ["January", "March", "May", "July", "August", "October", "December"]:
	print("No. of days: 31 day")
else:
	print("Wrong month name")

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.

def change_string(x):
    if len(x)< 3:
        return x
    else:
        if x.endswith('ing'):
            x=x.replace('ing','ingly')
            return x
        else:
            x=x+'ing'
            return x

print(change_string('ab'))
print(change_string('surprising'))
print(change_string('study'))
