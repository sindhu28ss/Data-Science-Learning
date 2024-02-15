# 1. iteration structure

# while loop, infinite loop
x = 1
while True:
    print(x)
    x = x + 1
    
# while loop with conditions
x = 1
while x < 5:
    print(x)
    x = x + 1

# break in loop
x = 1
while True:
    print(x)
    x = x + 1
    if x >= 5:
        break

# for loop
for i in range(1,5):
    print("cheers!")

# for loop plus conditional statement
x = [1,3,4,5]
for i in x:
    if i > 2:
        print(i)

# calculate the largest number 
x = [43,34,22,32,62,12] # Of course, we can easily find it using max(x)
temp_largest = 0 # set up a temporary largest number
for i in x: # for each element in list x
    if i > temp_largest: # if that element i is greater
        temp_largest = i # we update the temp_largest
print(temp_largest)
    
# continue method, pass the current iteration
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print('Current Letter :', letter)
   
# another continue example
var = 10
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print('Current variable value :', var)
print("Good bye!")

# count the number of even and odd numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Declaring the list
count_odd = 0 # setup a counter for odd numbers
count_even = 0 # setup a counter for even numbers
for x in numbers:
        if x % 2 == 0: # if the remainder is 0 (even number) 
    	     count_even+=1 # add 1 to the even number count (count_even = count_even + 1)
        else:
    	     count_odd+=1 # otherwise add 1 to the odd number count
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

'''
######## Exercise 1 ########
count how many numbers between 1500 and 2700 that are divisible by both 5 and 7

'''
count=0
for i in range(1500,2701):
    if i%5==0 and i%7==0: #condution to check if the number is divisible by both 5&7
        count+=1
print("Nos divisible by both 5 and 7:",count)


# count the number of letters/digit/others in a string
x = 'Python3.0' 
num_letter=0 # set up a counter to count the number of letters 
num_digit=0
num_other=0

for i in x: # for each character in string x 
    if i.isalpha(): # if that character is a letter
        num_letter += 1 # add 1 to that counter 
    elif i.isnumeric():
        num_digit+=1
    else:
        num_other+=1
print(num_letter,num_digit,num_other)


# Write a Python program to create the multiplication table (from 1 to 10) of a number.
n = 3
for i in range(1,11):
   print(n,'x',i,'=',n*i) # this can also be print(n+'x'+str(i)+'='+str(n*i))


''' ######## Exercise 2 ########'''
# Write a Python program to construct the following pattern, using a nested loop number.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

''' _______________________________________________'''

for i in range(1,10):
    for j in range(i):
        print(i,end='')
    print()
        
# given two lists, generate a list containing the common elements from both lists
# First, we can use the set operation:

import random
common=[]
a = range(1, random.randint(1,30))
print(a)
b = range(1, random.randint(10,40))
print(b)
print(set(a)&set(b))

# Or, we can use the append command
common=[]
a = range(1, random.randint(1,30))
print(a)
b = range(1, random.randint(10,40))
print(b)
for i in a:
    if i in b:
        common.append(i)
print(common)

# enumerate in iteration
x=['1st entry','2nd entry']
for i,entry in enumerate(x):
     print(i) # the index of iteration we are currently at
     print(entry) # the iterator
    
# another enumerate example 
L = ['apples', 'bananas', 'oranges']
for idx, val in enumerate(L):
  #print("index is %d and value is %s" % (idx, val))
  print("index is {} and value is {}".format(idx, val))
  
  
# another enumerate example
str1 = "Python"
for idx, ch in enumerate(str1):
  print("index is %d and character is %s" \
         % (idx, ch))
		 
''' ######## Exercise 3 ########'''
# show the immediately repeated letters in a string
x="apple is a healthy food"

''' _______________________________________________'''

x="apple is a healthy food"
len(x)
repeated_letters={}
for index,value in enumerate(x[:-1]):
    if value==x[index+1]:
        print("index is %d and character is %s" % (index, value))
        repeated_letters[index]=value
print(repeated_letters)

# backward iteration
# using reversed
for items in reversed([1,2,3,4]):
    print(items)

# or 
for items in [1,2,3,4][::-1]: # [::-1] is also reversing a list
    print(items)
	
# using steps in range
for items in range(20,0,-2):
    print(items)
# --------------------------------------------------------------------------------------
# 2. inline iteration

f=[x for x in range(1,10)]
print(f)

# given two lists, generate a list containing the common elements from both lists
x=[1,2,3,4]
y=[2,4,5,5]
print([i for i in x if i in y])
print([i for i in x if i not in y])

# inline iteration with tuples
g=[(x,y) for x in range(1,4) for y in range(5,7)]
print(g) # for each x, populate all possible y

r=[(x,y) for x in range(1,4) for y in range(x+1,x+3)]
print(r)

tuple_list=[(1,2),(3,4),(5,6)]
j=[(x**2+1,y) for (x,y) in tuple_list]
print(j)

x=[1,2,3]
y=[4,5,6]
z=[x/y for x,y in zip(x,y)]
print(z)


''' ######## Exercise 4 ########'''

# given two lists, generate a dictionary containing elements of x as keys 
# and the elements of y as values

x=[1,2,3]
y=[4,5,6]
z={i:j for i,j in zip(x,y)}
print(z)


# flatten a list of list into a single list
x=[[1,2,3],[3,4,5]] # the result should be [1,2,3,3,4,5]
y=[i for s in x for i in s]
print(y)

#--------------------------------------------------------------------------------------
# 3. An example, rock paper, scissors
 
# rock paper scissors
# define the choice space 
space=['rock','scissors','paper']

# define syster input
def RCP_game(input_value):
    import random
    space=['rock','scissors','paper']
    sys_input=random.sample(space,k=1)[0]# the sample function returns a list
    print(sys_input)

# define user input
    user_input=input_value

# if tie, continue
    while sys_input==user_input:
        sys_input=random.sample(space,k=1)[0]
        user_input=input('tie, please make another choice: ')
    
    print('you {}. '.format(user_input))
    print('system {}.'.format(sys_input))

    if ((sys_input=='scissors' and user_input=='rock')|(sys_input=='paper' and user_input=='scissors')
        |(sys_input=='rock' and user_input=='paper')):
        print('you win')
    else:
        print('you lose')
        

RCP_game('paper')
RCP_game('rock')
RCP_game('scissors')
# --------------------------------------------------------------------------------------
# 4. An example, guessing numbers
''' ######## Exercise 6 ########'''

# wrtie code to guess a randomly generated number from 0 to 9

def guess_a_number(user_input):
    import random
    sys_number=random.randint(0,9)
    count=1
    while user_input!=sys_number:
        if user_input>sys_number:
            count+=1
            user_input=int(input('too big, please enter again: '))
        elif user_input<sys_number:
            count+=1
            user_input=int(input('too small, please enter again: '))
    print('correct answer in {} guesses'.format(count))

user_input=int(input('please enter your choice from 0 to 9: '))
guess_a_number(user_input)


user_input=int(input('please enter your choice: '))

import random
sys_number=random.randint(0,9)
count=1
while user_input != sys_number:
    print("Wrong guess. Please Try again.")
    user_input = int(input('Please enter your choice between 0 and 9: '))
    count += 1

print('correct answer in {} guesses'.format(count))

''' _______________________________________________'''


''' ######## Exercise 7 ########'''
# --------------------------------------------------------------------------------------
# 5. length of nested list

# len([1, [2, 3]]) will equal to 2
# here we want to know know many items are there in the nested list. 
# The answer to the question is 8. 

x=[[1,2,3],[3,4,5],7,[5]]
print(len(x[0]))
print(len(x[1]))
print(len(x[3]))
count=0
for i in x:
    if (type(i)==int):
        count+=1
    else:
        count+=len(i)
print(count)

x=[[1,2,3],[3,4,5],7,[5]]
#print(len(x[0]))
#print(len(x[1]))
#print(len(x[3]))
count=0
for i in x:
    if isinstance(i,int):
        count+=1
    else:
        count+=len(i)
print(count)

''' _______________________________________________'''

# --------------------------------------------------------------------------------------
# 6. word guessing game
# the system generates a word (such as banana) and the user starts to guess letter by letter
# if the user guessed one correct letter (such as a), 
# the system shows the current progress to the user such as (_a_a_a)
# the user only has limited turns. The number of turns left is reported to the user
# if all letters are correctly guessed, say "you won!".

import random

def display_word(word, guessed_letters):
    display = ''
    for char in word:
        if char in guessed_letters:
            display += char
        else:
            display += '_'
    return display

# List of potential words
words = ["banana", "apple", "cherry", "strawberry", "blueberry"]

# System selects a random word
word_to_guess = random.choice(words)

# Variables to track progress and turns
guessed_letters = []
turns_left = len(word_to_guess) + 3  # For simplicity, I'm giving the user 3 extra turns.
won = False

print("Welcome to the Word Guessing Game!")
print(f"You have {turns_left} turns to guess the word!")

while turns_left > 0 and not won:
    guess = input("Guess a letter: ")
    
    # Check if the letter has been guessed before
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)
    
    # Display current progress
    current_display = display_word(word_to_guess, guessed_letters)
    print(current_display)
    
    if "_" not in current_display:
        won = True
        print("Congratulations, you won!")
        break
    
    # Decrease turns
    turns_left -= 1
    print(f"You have {turns_left} turns left.")
    
if not won:
    print(f"Sorry, you're out of turns! The word was '{word_to_guess}'")

#---------------------------------------------------------------------------------           
    
# define a function to check the postion of a character in a string as a list
def position(word,char):
    positions = []
    for idx,c in enumerate(word):
        if char == c:
            positions.append(idx)
    return positions

# initialize
position('python','h')
position('sindhu','s')
# --------------------------------------------------------------------------------------
# 7 binary search algorithm for sorted list
# Binary Search is a searching algorithm for finding an element's position in a sorted array.
# https://www.programiz.com/dsa/binary-search

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
 
        mid = (high + low) // 2 # the integer part of the division
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
 
# Test array
arr = [ 2, 3, 4, 5, 40 ]
x = 40

arr = [ 10, 11, 13, 20, 22 ]
x = 20
 
# Function call
result = binary_search(arr, x)
print(result) 

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
#--------------------------------------------------------------------------------------
# 8. change iterating range on the go
# example1: iteration is finite since the values added to the list will not trigger further adding
x=[1,2,3,4]
for i in x:
    print(i)
    if i%2==0:
        x.append(i+1)
print(x)

# example2: iteration is infinite since the values added to the list will trigger further adding
x=[1,2,3,4]
for i in x:
    print(i)
    if i%2==0:
        x.append(i+2)
print(x)
        
# example3: iteration is infinite since as we add 4 to the begining of the list, 
# the next number is still 2, not 3. So we keep adding 4 to the front.
x=[1,2,3,4]
for idx,v in enumerate(x):
    print("the index is: ",idx, "the value is: ",v)
    if v%2==0:
        x.insert(0,v+2) # insert the value to the index
        
# --------------------------------------------------------------------------------------


''' ######## Exercise 8 ########'''

# 9. more examples for iterations.

# 9-1
# You have a dictionary with years 2015-2020 as keys and 
# some albums released for each year as key values. 
# Write a function that takes an album and returns the year in which it was released.
# For example, if I input "Honeymoon", the function should return 2015
album_dict = {
  2015: ("Vulnicura", "Honeymoon", "Rebel Heart"),
  2016: ("Lemonade", "Blackstar", "A Moon Shaped Pool"),
  2017: ("Flower Boy", "Antisocialites"),
  2018: ("El Mal Querer", "Someone Out There", "Cranberry", "Kamikaze"),
  2019: ("thank u next", "Magdalene", "Ode to Joy"),
  2020: ("Rough and Rowdy Ways", "folklore", "Future Nostalgia", "Colores")
}
user_input=input("Please enter the Name of the Album:")
for key,value in album_dict.items():
    if "Honeymoon" in value:
        print("The year is:",key)

''' _______________________________________________'''

''' ######## Exercise 9 ########'''

#9-1
# Merge the dictionaries for keys ranging from 0 to 9
# answer should be {0: 'c', 1: 'd', 2: None, 3: None, 4: None, 5: 't', 6: None, 7: None, 8: None}

dct=dict.fromkeys(list(range(9)),None)
x={0:"c",1:"d",5:"t",9:"r"}

for key in dct:
    if key in x:
        dct[key] = x[key]

print(dct)

# 9-2
# given some numbers stored in a tuple such as operands=(2, 3, 5, 75). And a given target value such as target =158.
# please find ways to achieve the target value using the given numbers. For example, 75*2+3+5=158

from itertools import permutations, product
operands = (2, 3, 5, 75)
target = 158
count=0
# Loop through all permutations of operands
for perm in permutations(operands):

    # For each permutation, loop through combinations of arithmetic operations
    for ops in product(('+', '-', '*', '/'), repeat=len(operands)-1):
        
        # Build an expression using the operands and operations
        expression = ''.join(str(perm[i]) + ops[i] for i in range(len(ops))) + str(perm[len(ops)])
        
        # Evaluate the expression
        try:
            if eval(expression) == target:
                count+=1
                print(f"{expression} = {target}")
        except ZeroDivisionError:
            pass 
print(count)
        
        