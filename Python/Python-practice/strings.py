
fruit="banana"

length=len(fruit)
print(length)

last=fruit[length-1]
print(last)

#-----------------------------------------------------------------------
#print all the letters using while loop:
    
index=0
while index < len(fruit):
    letter=fruit[index]
    print(letter)
    index=index+1

#print all the letters using for loop:

for i in fruit:
    print(i)
#----------------------------------------------------------------------   

def reverse_print(s):
    for char in reversed(s):
        print(char)

input_string = "hello"
reverse_print(input_string)
reverse_print('sindhu')

for char in fruit:
    print (char)
    
#-----------------------------------------------------------------------

'''find ()  function'''

def find(str, ch):
    index = 0
    while index < len(str):
        if str[index] == ch:
            return index
        index = index + 1
    return -1
    
find('sindhu','u')
find('sindhu','a')
find('preethi','e')


def find(word, letter, start_index=0):
    index = start_index
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

# Test the function
word = "banana"
letter = "a"
start_index = 2
start_index = 6

print(find(word, letter, start_index))

x='karthik'
print(x.find('a'))

#-----------------------------------------------------------------------------------

'''Looping and counting
The following program counts the number of times the letter a appears in a string'''

fruit='banana'
count = 0

for char in fruit:
    if char == 'a':
        count+= 1
print(count)
    
'''As an exercise, encapsulate this code in a function named
countLetters, and generalize it so that it accepts the string and the
letter as arguments'''


def countLetters(word, char_to_count):
    count = 0
    for char in word:
        if char == char_to_count:
            count += 1
    return count

# Test the function
word = "banana"
letter = "a"
print(countLetters(word, letter))

'''As a second exercise, rewrite this function so that instead of traversing
the string, it uses the three-parameter version of find from the
previous'''

    
def countLetters(word, char_to_count,start_index):
    count = 0
    for char in word[start_index:]:  
        if char == char_to_count:
            count += 1
    return count

# Test the function
word = "banana"
letter = "a"
start_index=2

print(countLetters(word, letter,start_index))

#-----------------------------------------------------------------------

fruit = "banana"
index = fruit.find("a")
print (index)

fruit.find("na")

fruit.find("a",3)

fruit.find("na",3)

fruit.find("b",1,2)

fruit.find("b",0,2)




























