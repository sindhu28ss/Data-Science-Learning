'''As an exercise, write a compare function that returns 1 if x>y 
#0 if x == y, and -1 if x < y'''

def compare(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1

compare(9,8)
compare(4,4)
compare(7,9)

'''hypotenuse that returns the length of the hypotenuse of a right triangle
given the lengths of the two legs as arguments. Record each stage of
the incremental development process as you go'''

import math
def hypotenuse(a,b):
    c=int(math.sqrt((a**2)+(b**2)))
    return c

hypotenuse(3,4)


def absoluteValue(x):
    if x < 0:
        return -x
    elif x > 0:
        return x

print(absoluteValue(0))


'''As an exercise, write a function slope(x1, y1, x2, y2) that returns
the slope of the line through the points (x1, y1) and (x2, y2). Then use
this function in a function called intercept(x1, y1, x2, y2) that
returns the y-intercept of the line through the points (x1, y1) and
(x2, y2)'''


def slope(x1,y1,x2,y2):
    m=((y2-y1)/(x2-x1))
    return m

def intercept(x1,y1,x2,y2):
    m=slope(x1,y1,x2,y2)
    y_intercept=y1-m*x1
    return y_intercept

x1, y1 = (1, 2)
x2, y2 = (3, 4)

print("Slope:", slope(x1, y1, x2, y2))
print("Y-Intercept:", intercept(x1, y1, x2, y2))

#Boolean functions:
    
def isDivisible(x,y):
    if x % y == 0:
        return True
    else:
        return False
    
isDivisible(6, 4)
isDivisible(6, 3)


'''Rewrite your pay computation with time-and-a-half for overtime and 
create a function called computepay which takes two parameters
 ( hours and  rate)'''


def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
        return pay
    else:
        pay = hours * (rate+(rate/2))
        return pay

x=int(input("Enter Hours:"))
y=int(input("Enter Rate:"))
computepay(x,y)

#-------------------------------------------------------------------

'''Arbitrary arguments, * args'''

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#--------------------------------------------------------------------
'''keyword arguments'''

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#-----------------------------------------------------------------------

'''Arbitrary Keyword Arguments, **kwargs'''

def my_function(**kid):
  print("First name is " + kid["fname"])  
  print("Last name is " + kid["lname"])
  
my_function(fname = "Sindhu", lname = "Sudhakar")

#--------------------------------------------------------------------

'''Default Parameter Value'''

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#---------------------------------------------------------------------

'''Passing a List as an Argument'''

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#------------------------------------------------------------------

#The pass Statement
'''function definitions cannot be empty, but if you for some reason have a function definition with no content, 
put in the pass statement to avoid getting an error'''


def myfunction():
  pass

#---------------------------------------------------------------

'''Recursion
Python also accepts function recursion, which means a defined function can call itself'''

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#-----------------------------------------------------

























