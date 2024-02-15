# 1. Variables

# text data type
x='hello world'
print(type(x))
print(dir(x)) # Check the methods and attributes available for a particular class

# integer data type
x=5
print(type(x))
print(dir(x))

x=-5

# float data type
x=5.5
print(type(x))


# most common operations
x=5
print(x/5)
print(x*5)
print(x+x)
print(x-x)
print(x**2) # this is power function in python
y=-5
print(abs(y)) # calcualte absolute value


# boolean data type
x=True
print(type(x))


# dictionary type = a collection which is "ordered and changeable". No duplicate members.
x={"w":2}
print(type(x))

x.keys()
x.values()

y={"w":2,"x":3,"y":4}
y.keys()
y.values()


# set = a collection which is "unordered, unchangeable", and unindexed. No duplicate members.
x={"w",2}
print(type(x))


# list can have multiple occurrences of the same element and store unordered values.
x=["w",2]
print(type(x))
print(x)

# tuples are immutable
x=("w",2)
print(type(x))


# concatenation in print function
print("Were" + "wolf")
print("Door" + "man")
print("4" + "chan")
print(str(4) + "chan") # the str() method convert viable variables to a string
print(4 * "test") # repeating
print(4+"test") # this will give error

# input value/parameter through console
name = input("Give me your name: ")
name = input()
print("Your name is " + name) # this is how to concatenate strings in python

# calculate area of circle given input radius
from math import pi
r = float(input ("Input the radius of the circle : ")) # pi * r^2
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
integer=input('please enter the integer:')
a=int(2*str(integer))
print(a)
b=int(3*str(integer))
print(b)
value=int(integer)+a+b
print(value)

7/3
# quotient and remainder
quotient = 7 // 3
print(quotient)
remainder = 7 % 3
print(remainder)

# order of calculation
# parenthesis  have the highest precedence 
print((1+1)**(5-2))
# exponentials have the next highest precedence
print(2**1+1)
print(3*1**3)
# * and / have the same precedence
# + and - have the same precedence
# when operators have the same precedence, execute from left to right
print(5-3-1) # the result is 1, not 3.

# calcuation from imported packages

import math

x=3.4
print(math.ceil(x))
print(math.floor(x))
print(math.factorial(3))
print(math.exp(3))
print(math.pow(3,4))
print(math.sqrt(4))

# some constants
print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)
# ----------------------------------------------------------------------------------------
# 2. logical operation

# logical value generated from comparison
x=1
print(x>0)

y= 2>1
print(y)

x=2
y=2
z=3
print(x==y)
print(x==z)

s=True & False
print(s)
s=False & True
print(s)
s= True & True
print(s)

t=(2>1)&(3>2)
print(t)

w=True | False
print(w)

u=(2>1)|(3>4)
print(u)

v = not False
print(v)

v = not (1>3)
print(v)

# what is the difference between "and" and "&"?
# for boolean values they work the same.
# but check the following:
    

print(3 and 4)
print(0 and 4)
# the "and" uses lazy execution, meaning that if it finds a false, it stops executing and return the current value (false)
# here, 3 and 4 are both treated as true, so it will check until the last value and return it, which is 4
# print(0 and 4) returns 0 because 0 is treated as false, so it stops executing and returns that value 0.


print(3 & 4)
# & performs the bitwise calculation, for example 3 is 011, and 4 is 100, so bitwise calculation gives 000, which is 0.

print(4 & 4)
print(4 & 7) # 4 is 100 and 7 is 0100
print(5 & 3) # 5 is 0101 and 3 is 011 

# falsy values are treated as false in and/or operation, below are the common falsy values
import numpy as np
print([] and 4)
print(() and 4)
print({} and 4)
print(dict() and 4)
print(0 and 4)
print(4 and None)# and 4)

# is and ==
list1 = []
list2 = []
list3=list1

print(id(list1))
print(id(list2))
print(id(list3))

print(list1==list2)
print(list1 is list2)
print(list1 is list3)

list3=list3+list1

# they are actually different object, but value is the same
print(id(list1))
print(id(list2))
print(id(list3))

print(list1 is list3)
print(list3 is [])
print(id([]))
print(list3==[])

# object instantiation and copy
x=[1,2,3]
print(id(x))
y=x
print(id(y))
x[1]=5 # new object is not instantiated, the id of x does not change
print(id(x))
print(y)

x=[1,2,3]
print(id(x))
y=x
print(id(y))
x=[3,2,1] # new objects are instantiated, the id of x changes
print(id(x))
print(y)
print(id(y))
# we can use copy() to force instantiating a different new object when doing y = x
x=[1,2,3]
print(id(x))
y=x.copy()
print(id(y)) # now y has a different id from x
x[1]=5 
print(id(x))
print(y)
print(id(y))

# ----------------------------------------------------------------------------------------
# 3 naming variables

#some variable names are illegal

123word="word" # variable names cannot start with a number
word%123="word" # don't add special characters in variable names
class="word" # cannot use python key words as variable names
# the interpretor uses key words to recognize program structures.


# There are 33 keywords
#and del from None True
# as elif global nonlocal try
# assert else if not while
# break except import or with
# class False in pass yield
# continue finally is raise
# def for lambda return

# But other built-in functions can be used as variable names
dict=34
print(dict)
# however, it is still recommended to avoid using them
# ----------------------------------------------------------------------------------------
# 4 three common errors

# syntax error my_var=123
bad name = 5 # python thinks an operator is missing between two variables bad and name
month=09 # invalid token, 0 is not allowed before a number.

# variable not defined
# usually happens when you misspell variable names
principal = 327.68
interest = principle * rate

# index out of bound
x=(1,2,3)
print(x[3]) #python starts from 0!

x=[]
print(x[0])
# ----------------------------------------------------------------------------------------
# 5. error handling

# does not interrupt the program, while trace the source of error
x=1
y=0
try:
    print(x/y)
except:
    print("something is wrong")

# after you see that the error code is called "ZeroDivisionError"
# you can rule out this error using

x=1
y=8
x='1'
y=8
x=1
y=0
try:
    print(x/y)
except ZeroDivisionError:
    print("division by zero")
except TypeError:
    print("type error")
except:
	print("unknown error")
	
# print system generated error message

try:
    a = 1/0
except Exception as e:
    print(e)
    
# ----------------------------------------------------------------------------------------
# 6. import library

# import library then use its methods
import statistics
print(statistics.mean([1,2,3]))


# import methods directly
from statistics import mean, median
print(mean([1,2.4,3]))
print(median([1,2.4,3]))

# ----------------------------------------------------------------------------------------
# 7.. directory

import os
print(os.listdir()) # printing all files in the current directory
os.chdir('/Users/sindhujaarivukkarasu/Documents/BAN 601 Tech Fund/class python programs') # change the working directory
print(os.listdir('.')) # the current folder
print(os.listdir('..')) # the parent folder
print(os.listdir('../Python-practice')) # the neighboring folder

# ----------------------------------------------------------------------------------------
# 8. installing libraries

# 1 pip isntall
# go to environment->open terminal->pip install celery
# in the spyder console->pip install celery

# 2 using conda install
# search online for conda cloud celery 
# copy the code to the termnal and run.

# Both pip and conda are package management systems.
# they are other package management systems such as npm and yarn. 
# ----------------------------------------------------------------------------------------
# 9. comments

# single line comments: #

# multiline comments:

'''
this is a multi-line
comment
'''
# ----------------------------------------------------------------------------------------
# 10. pass statement

# sometimes you want to draft the structure of your program but you want to fill in the details later, 
# you can use pass statement in such time

# Sequential
def function_1(x, y):
    a= x+y
    return a

  
function_1(1, 3)
    
# repeated 
for i in range(1,10):
    x =0
    x += i
    print(x)


# conditional 
x =2
y =1

if x>y:
    print("x is bigger")
else:
	print("y is bigger")
	
class Employee:
	pass
# ----------------------------------------------------------------------------------------
# 11. modules

# create two files one is main.py, inside which write the code
import module

# the other file is module.py, inside which write the code
print("hello")
print(__name__)
if __name__=="__main__":
    print("now running the module itself")

# check what __name__=="__main__" does.


# if in the main module you do import multiple times
import module
import 
# then only one hello will be printed, the imported module is only run once when it is first imported.


# now try another example
# in the module.py, write:
def func(x):
    return x+1
# in the main.py, write
import module
print(module.func(4))
# then try run it in the main
# we can achieve similar thing by doing the following:
from module import func
print(func(8))


# variables can also be imported
# in the module, write down the following:
x=4
# in the main, write down the following:
from module import x
print(x) # the value of x is imported from the module
# you can achieve similar things using the following in the main.py
import module
print(module.x)


# import a class from a mudule
# in the module, write
class car:
    
    def add(self,x):
        return x+1
		
# in the main.py. write
import module

car1=module.car()
print(car1.add(4))
# ----------------------------------------------------------------------------------------
# 12.  using terminal to execute python scripts

# first cd to the working directory

# create a script that contains the following
print("hello world")
# then you can save it as "python script_name.py" to execute the script


# create a script that contains the following:
import sys
if __name__=="__main__":
    print(sys.argv)
# then in the terminal type "python filename"
# this is way to pass terminal variables to the python program
# ----------------------------------------------------------------------------------------
# 13. environment variables

# suppose we will use our password in the code, but we don't want to hard code the password in the program
# one way is to put the password to the environment variable
# create one .env file in the working directory, and inside, put the following inside:
password=1234
accountnum="Inkyu"
available_ram=16
userprofile="C:\path_to_profile"
# userprofile="/Users/inkyukim"


# then in the main script, use the following to access the password and account number
import os
#pip install python-dotenv
from dotenv import load_dotenv

load_dotenv("test.env")

password=os.getenv("password")
account=os.getenv("accountnum")

print(password)
print(account)
# ----------------------------------------------------------------------------------------
# 14. configuration files

# used to declare some frequently used constants used in your project development
# yaml is a very common standard
# create a config.yaml file, and inside, put
account1:
    URL: '127.0.0.1:1234'
    id: '4321'
account2:
    URL: '127.0.0.1:4321'
    id: 1234
serverlist: [1,2,3,4]

# then in the main file, use the following to access the configuration

import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

print(config)
print(config["account1"]["URL"])
print(config["serverlist"])

# difference between .env and .yaml
# environment variables is usually information about the development and deployment environment. 
# While config variables include information specifically on the current application.


# json is another commonly used format
# first create a file called config.json that contains the following:
# {
#     "mysql":{
#         "host": "127.0.0.1",
#         "user": "root",
#         "password": 123,
#         "database": "employee"
#     },
#     "other":{
#         "first":1,
#         "second":2        
#     }
# }

# in the script, accessing the data using the following

import json

with open("config.json") as f:
    config = json.load(f)
    
print(config["mysql"]["host"])
# ----------------------------------------------------------------------------------------
# 15. console and terminal

# console is a place to:
# 1, show output and error messages of the current session
# 2, take user input
# 3, work as a shell, you can actually program in it


# terminal is a place where you can interact with the file system, operating system, and your current project at the same time
# some example: 
# 	cd /  -> home directory
# 	cd path -> get into a path
# 	dir -> show files in the path
# 	mkdir new_folder -> create a new folder
# 	> test.txt -> create a new file 
# 	rm test.txt -> delete a file 
# 	rmdir new_folder -> delete a folder
# 	cd ../ -> go to parent directory 
# 	netstat -an -> show all web application connections and port usage 
# 	ipconfig  -> show configuration of your current networ
# 	set -> show all environment variables
# 	test network connection -> ping 8.8.8.8  that is the google dns. Enable and disable the wifi to check the difference
# 	or ping csueastbay.edu(ctrl+c to stop it)
# ----------------------------------------------------------------------------------------
# 15. homework formatting

# task 1

# code

# task 2

# code

# All tasks should be answered within the same .py script, or if you prefer, the .ipynb. script.




