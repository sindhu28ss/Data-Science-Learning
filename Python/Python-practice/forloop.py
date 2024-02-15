#For loops
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#The for loop does not require an indexing variable to set beforehand.
#Looping Through a String
for x in "banana":
  print(x)
  
#The break Statement-we can stop the loop before it has looped through all the items
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
#The continue Statement - we can stop the current iteration of the loop, 
#and continue with the next'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
#The range() Function - To loop through a set of code a specified number of times
#returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
#and ends at a specified number

for x in range(6):
  print(x)
  
for x in range(2, 6):
  print(x) 
  
#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
  print(x)  
  
#Else in For Loop - specifies a block of code to be executed when the loop is finished
for x in range(6):
  print(x)
else:
    print("Finally finished!")  
  
#The else block will NOT be executed if the loop is stopped by a break statement.
  
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

  
#Nested Loops - a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop" 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)  
  
#The pass Statement'''

for x in [0, 1, 2]:
  pass
  
  
  