#input() method to get an input from user
print('What is your name?')
name=input()
print (f"Good Morning Beautiful, {name.title()}!")

name=input('What is your name? ')
color=input('What is your favorite color? ')
print(name+' likes '+color)

#input() accepts string values by default
#so converting the type to int
age=int(input('what is your age?'))
print(age)

#-----------------------------------------------------------------------------

#title()-converts the first name of your name to uppercase

name="sindhu"
print(name.title())

#upper() -converts letters to uppercase
name="sindhu"
print(name.upper())

#lower()-converts letters to lowercase
name="SINDHU"
print(name.lower())

#find() returns the index of the first occurrence of the string
name='shree'
print(name.find('e'))
print(name.find('t')) #returns -1 if its not found

#replace() - replaces a string value with another
name='shree'
print(name.replace('e','i'))

#len() to calculate the length
name='sudhakar'
print(len(name))

#in operator checks if the specified sequence of string is present in the variable
name='Python for Beginners'
print('Python' in name) #returns True
print('python' in name) #returns False, case sensitive

#------------------------------------------------------------------------------

#using variables in a string
first_name="sindhuja"
last_name="sudhakaran"
full_name=f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")
message=f"Hello,{full_name.title()}!"
print(message)

#Adding whitespace to strings with tabs or newlines
print("python")
print("\tPython")

#To add a newline in a string, use the character combination \n:
print("Languages:\nPython\nC\nJava")

#To combine\n\t
print("Languanges:\n\tPython\n\tC\n\tJava")

#To trim extra spaces from right end of a string: rstrip()
favorite_language='Python '
print(favorite_language)
print(favorite_language.rstrip())


#To trim extra spaces from left end of a string: lstrip()
favorite_language=' Python'
print(favorite_language)
print(favorite_language.lstrip())

#To trim extra spaces from both sides of a string: strip()
favorite_language=' Python '
print(favorite_language)
print(favorite_language.strip())


#apostrophe and single quote
message="One of Python's strength is its diverse community"
print(message)
#message='One of Python's strength is its diverse community''

#format strings:
    
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Escape character:allows you to use double quotes when you normally would not be allowed
txt = "We are the so-called \"Vikings\" from the north."


#retrieving values by index in a string
course='python for beginners'
print(course[0])
print(course[1])
print(course[-1])
print(course[-2])
print(course[0:3]) #retrieves from 0 till 2nd value
print(course[0:]) #retrieves all the characters from the beginning
print(course[1:]) #retrieves all the characters starting from index 1
print(course[:5]) #retrieves all the characters from the beginning till 4th index
print(course[:]) #retrieves all the characters
new=course[:]
print(new)

name='Jennifer'
print(name[1:-1])


#task-------------------------------------------------------------------------
quote="Albert Einstein once said, A person who never made a mistake never tried anything new."
print(quote)

famous_person="Albert Einstein"
quote="A person who never made a mistake never tried anything new."
message=f"{famous_person} once said, {quote}"
print(message)


name=" sindhu"
print(name)
print(name.lstrip())
name="sindhu "
print(name)
print(name.rstrip())
name=" sindhu "
print(name)
print(name.strip())

#------------------------------------------------------------------------------

#Booleans:

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

'''Most Values are True

Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones'''

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

'''Some Values are False - there are not many values that evaluate to False, except empty values, such as (), [], {}, "", 
the number 0, and the value None.
And of course the value False evaluates to False'''

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Functions can Return a Boolean

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

'''Python also has many built-in functions that return a boolean value, 
like the isinstance() function, which can be used to determine if an object is of a certain data type'''

x = 200
print(isinstance(x, int))

#----------------------------------------------------------------------------------------------------------

#Integers

print(2 + 3)
print(3-2)
print(2*3)
a=8/2 #returns quotient in float
print(a) 
print(type(a))
b=8//2 #returns quotient in int
print(b)
print(type(b)) 
print(8%2) #returns remainder

# ** means power of

print(3**2)
print(3**3)
print(10**6)


# Floats

print(0.1+0.1)
print(2*0.1)
print(2*0.2)
print(0.2+0.1)
print(3*0.1)

print(1+2.0)
print(2*3.0)
print(3.0**2)

#augmented assignment operator

x=10
x+=3
print(x)
x-=3
print(x)

#order of operations

print(2+3*4)
print((2+3)*4)

#underscores in numbers: python only points 

universe_age=14_000_000_000
print(universe_age)

#multiple assignments

x,y,z=0,1,2
print(x)
print(y)
print(z)

#constants

MAX_CONNECTIONS=5000

#-------------------------------------------------------------------------

#math functions

#round() - rounds off its value

x=3.5
print(round(x))

#abs() - returns absolute value
x=9
print(abs(-9))

import math

x=2.9
print(math.ceil(x)) #rounds up the value

print(math.comb(10, 5)) #comb(n,k)=n!/(k!*(n-k)!), when k<=n 
#evaluates to 0, when k>n

print(math.comb(3,5)) #0, becoz k>n

#returns a float with abs value of x, but with the sign of y
#math.copysign(x,y)
print(math.copysign(1.0,-0.0)) 

#abs value of x
x=-4.5
print(math.fabs(x))

print(math.factorial(5)) #factorial math.factorial(n)


print(math.floor(6.7)) #rounded down value

#-----------------------------------------------------------------------------






































