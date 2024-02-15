# 1. defining functions

# create a function that convert from fahrenheit to celsius
def f_to_c(fahrenheit): # we call this function f_to_c, the input is fahrenheit degree.
    celsius = (fahrenheit - 32) * 5/9 # calculate the celcius degree
    return celsius # return the output value, the calculated celsius degree
print(f_to_c(75)) # after defining the f_to_c function, let's call it to convert 75 fahrenheit to celsius

# defining a function that reverse a given string
def reverse(text):
    reversed_string="" # define an empty string, append letter one by one to it later
    for i in text: # for each letter in text. 
        reversed_string=i+reversed_string # append the letter to the front of reversed_string
    return reversed_string # return the reversed string
    
print(reverse('helloworld')) # call the reverse function, and print out the result.

# defining a function that tells if a given string is a palindrome or not.
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	while right_pos >= left_pos: # compare each position until right position is no longer greater than left position
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True # when going through the while loop without return False, we return True
print(isPalindrome('madam')) 

# variable numbers of inputs
## Single asterisk as used in function declaration allows 
## variable number of arguments passed from calling environment.
import statistics
def function(*sales):
    #return(sales)
    return(statistics.mean(sales))
print(function(1,2,3,4))

# set up default values for a function parameters
def function(x,y,z=1): # there are 3 parameters, if the third parameter is not provided, the default value is 1.
    return(x,y,z)
print(function(1,2))
print(function(1,2,3))
print(function(y=1,z=2,x=3))
print(function(1,2,z=3))
print(function(x=1,y=2,3)) # this will be an error. 
                            # Once we have a value assignment with variable names, 
                            # all variable value assignments must also come with the variable names
print(function(z=3,1,2)) # this is an error too.
print(function(1,z=3)) # error, we don't have input for the y

# void functions. It only performs some calculations but does not provide any outputs
def function(x,y): 
    print(x+y)
function(1,1)


# values defined within function are local variables. It will not affect variables defined outside the function.
def function(x,y): 
    z=3
    print(z)
function(1,1)
print(z) # value not defined error

# another example
z=0
def function(x,y): 	
    z=3
    return z
print(function(1,1))
print(z)	

# after declaring global variable. It overides the same variable names
# A global variable is a variable type that is declared outside of a function
x = 1
def f():
    global x
    x = 2
print(x)
f()
print(x)

# functions can use global variables defined outside of it
x = 1
def f():
    global y
    y=x
    z=x*y
f()
print(y)
# --------------------------------------------------------------------------------------------------------------
# 2. lambda functions

# lamda functions are short, anonymous functions.
x=lambda a: a**2
print(x(4))

# you can also use two parameters
x=lambda a,b: a**b
print(x(4,2))

# you don't even have to give them a name
print((lambda x, y: x + y)(5, 3))

# when they are useful
# when the function needs a function as an argument. 
# It's useful when we want to define a function and pass it into another function immediately
# suppose we want to sort a list based on the squared value 
def square(x):
    return x**2

print(sorted(range(-5, 6), key=square)) # the key parameter in the sorted function is to pecify a function 
      # (or other callable) to be called on each list element prior to making comparisons.
# we can also use lambda function
print(sorted(range(-5, 6), key=lambda x: x ** 2))

# the filter function, which needs a function to specify the filtering rule (must return a True or False)
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
filtered_list = list(filter(lambda num: (num > 7), numbers_list))
print(filtered_list)
# this the same as 
def x(y):
    return y>7
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
filtered_list = list(filter(x, numbers_list))
print(filtered_list)

# the map function, where we can map the iterable to some other iterable
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
mapped_list = list(map(lambda num: num % 2, numbers_list))
print(mapped_list)
# --------------------------------------------------------------------------------------------------------------
# 3. a closer look at the functions

# function object
def function():
    print("Hello world!")
print(function)

# method object
x=[1,2,3]
print(x.pop)

# assign method to a variable
x=[1,2,3]
y=x.pop
print(y) # printing the method id
print(y()) # calling the method
print(x)

# store function inside list and refer to them later
def fun1(x): return x+1
def fun2(x): return x-1
print(fun1.__name__) # the name attribute of the function object

operations=[fun1,fun2]
x=[1,2,3,4,5]

# suppose we are going to apply fun1 to odd position numbers and fun2 to even position numbers
for idx,num in enumerate(x):
    action=operations[idx%2]
    print(action.__name__+'({})'.format(str(num))+"="+str(action(num)))

# passing function into another function
def fun(x): 
    '''
    this is the function comment
    '''
    return "the input function is "+x.__name__
help(fun) # passing fun to help function, it shows the comment above the function
print(fun(fun)) # passing the funciton to itself

# define a funcion that accepts another function as inputs
def fun1(x): return x+1
def fun2(x): return x-1

def mainfun(func,x):
    return func(x)
print(mainfun(fun2,3))



# we can generate a series similar functions with lambda function
def fun(n): # the function returns a function given a parameter.
  return lambda a : a + n

plus1=fun(1) # the function that always add 1
plus2=fun(2) # the function that always add 2
# this will be so much faster. 

x=3
print(plus2(x))

