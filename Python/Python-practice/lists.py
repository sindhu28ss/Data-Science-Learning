#Lists
fruits=['apple','orange','kiwi','mango']
print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

#use title() to capitalize first letter 
print(fruits[1].title())

#use[-1] to get the last item in a list
print(fruits[-1].title())

#using individual values from a list
message=f"My favorite fruit is {fruits[1].title()}."
print(message)

#task-------------------------------------------------------------------------
names=['sindhu','sudhakar','priya','nisha']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print(f"Good morning, {names[0]}!")
print(f"Good morning, {names[1]}!")
print(f"Good morning, {names[2]}!")
print(f"Good morning, {names[3]}!")

trans=['cycle','bike','car','auto']
print(trans[0])
print(trans[1])
print(trans[2])
print(trans[3])

print(f"I love to ride a {trans[0]}")
print(f"I am planning to learn {trans[1]} driving this month")
print(f"My favorite brand of {trans[2]} is Mini Cooper")
print(f"{trans[3].title()} rides are cheaper and fun")
#-----------------------------------------------------------------------------

'''Change Item Value - refer to the index number'''

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

'''Change a Range of Item Values - To change the value of items within a specific range, 
define a list with the new values, and refer to the range of index numbers where you want to insert the new values'''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

'''If you insert more items than you replace, 
the new items will be inserted where you specified, 
and the remaining items will move accordingly'''

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
print(len(thislist))

'''Note: The length of the list will change when the number of items inserted 
does not match the number of items replaced

If you insert less items than you replace, the new items will be inserted where you specified, 
and the remaining items will move accordingly'''

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry","mango"]
print(len(thislist))
thislist[1:3] = ["watermelon"]
print(thislist)
print(len(thislist))

#------------------------------------------------------------------------------

'''insert elements in a list'''

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles=[]
motorcycles.insert(0,'ducati')
print(motorcycles)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#------------------------------------------------------------------------------

#applying elements to the end of the list-append()
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#append method to build an empty list
motorcycles=[]
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)

#------------------------------------------------------------------------------

'''Modifying elements in a list using index value'''
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)

'''Extend List - To append elements from another list to the current list, 
use the extend() method'''

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

'''Add Any Iterable - The extend() method does not have to append lists, 
you can add any iterable object (tuples, sets, dictionaries etc.)'''

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#------------------------------------------------------------------------------
#removing an item by value- remove() method

motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

#remove an item by value and using print statement
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} was too_expensive for me.")

'''If there are more than one item with the specified value, 
the remove() method removes the first occurance'''

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#--------------------------------------------------------------------------------------------------------------------

#remove an item using pop()method - removes the last item 
#but it lets you work with that item

motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#pop() method helps in print statement
motorcycles=['honda','yamaha','suzuki','ducati']
last_owned=motorcycles.pop()
print(f"The Motorcycle that I last owned was a {last_owned.title()}.")

#pop() method to remove an item by specifying the index
motorcycles=['honda','yamaha','suzuki','ducati']
first_owned=motorcycles.pop(0)
print(f"The motorcycle that I first owned was a {first_owned.title()}.")
print(motorcycles)

#-----------------------------------------------------------------

'''removing an item using the del keyword by specifying index value'''

motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[2]
print(motorcycles)

#The del keyword can also delete the list completely.

thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) - syntax error - undefined name 

#-------------------------------------------------------------

'''Clear the List - empties the list.
The list still remains, but it has no content'''

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#task-------------------------------------------------------------------------

guests=['karthik','priya','surya']
print(f"welcome to the dinner party, {guests[0]}!")
print(f"welcome to the dinner party, {guests[1]}!")
print(f"welcome to the dinner party, {guests[2]}!")

#replace
guests=['karthik','priya','surya']
print(f"{guests[0].title()} couldnt join us for the dinner today.")
guests[0]='Rajesh'
print(guests)
print(f"welcome to the dinner party, {guests[0]}!")
print(f"welcome to the dinner party, {guests[1]}!")
print(f"welcome to the dinner party, {guests[2]}!")

#insert & append
guests=['karthik','priya','surya']
print(guests)
print("I am glad that I found a bigger Dinner table, so we could invite more guests")
guests.insert(0,'sindhu')
print(guests)
guests.insert(2,'sudhakar')
print(guests)
guests.append('thara')
print(guests)
print(f"welcome to the dinner party, {guests[0]}!")
print(f"welcome to the dinner party, {guests[1]}!")
print(f"welcome to the dinner party, {guests[2]}!")
print(f"welcome to the dinner party, {guests[3]}!")
print(f"welcome to the dinner party, {guests[4]}!")
print(f"welcome to the dinner party, {guests[5]}!")

#pop() & del()
print(guests)
print("I can only invite 2 people for dinner")
removed1=guests.pop()
print(f"{removed1.title()}, We are sorry that we couldnt invite you to the dinner today")
print(guests)
removed2=guests.pop()
print(f"{removed2.title()}, We are sorry that we couldnt invite you to the dinner today")
print(guests)
removed3=guests.pop()
print(f"{removed3.title()}, We are sorry that we couldnt invite you to the dinner today")
print(guests)
removed4=guests.pop()
print(f"{removed4.title()}, We are sorry that we couldnt invite you to the dinner today")
print(guests)
print(f"{guests[0].title()}, you are invited for the dinner")
print(f"{guests[1].title()}, you are invited for the dinner")
print(guests)
del guests[0]
print(guests)
del guests[0]
print(guests)

#----------------------------------------------------------------------------

'''working with Lists

Loop Through the Index Numbers - You can also loop through the list items 
by referring to their index number

Use the range() and len() functions to create a suitable iterable'''

#findling the length of a list
cars=['bmw','toyota','honda','audi']
print(len(cars))

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Using a While Loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
'''Looping Using List Comprehension - offers the shortest syntax for looping through lists: 
    
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]''' #gives none


#For loop vs list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in fruits]

'''Iterable - The iterable can be any iterable object, 
like a list, tuple, set etc'''

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

#Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)

#Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#------------------------------------------------------------------    

#organizing a list

#sorting a list permanently with sort() method

cars=['bmw','toyota','honda','audi']
print(cars)
cars.sort()
print(cars)

#sort this list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#sorting a list temporarily with sorted() method

cars=['bmw','toyota','honda','audi']
print(cars)
print(sorted(cars))
print(cars)


#Sort Descending - reverse = True:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

print(cars)
cars.sort(reverse=True)
print(cars)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function by using the keyword argument key = function.

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


'''Case Insensitive Sort - By default the sort() method is case sensitive, 
resulting in all capital letters being sorted before lower case letters'''

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#So if you want a case-insensitive sort function, use str.lower as a key function:
#we can use built-in functions as key functions when sorting a list.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)   

#reverse() - does a complete reverse of the order of the list items

numbers = [8, 2, 10, 4, 5]
numbers.reverse()
print(numbers)

#If you want to reverse a list without modifying the original, you can use slicing:

numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print(reversed_numbers)  

#---------------------------------------------------------------

#looping through the entire list
#for loop - prints out each item in the list

magicians=['sindhu','sudhakar','karthik','priya']

for magician in magicians: 
    print(magician)
    
#doing more wih for loop-print messages
magicians=['sindhu','sudhakar','karthik','priya']
for magician in magicians:
    print(f"{magician.title()}, that's a great trick!")
    print(f"I cant wait to see your next trick,{magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

#Indentation error
magicians=['sindhu','sudhakar','karthik','priya']
for magician in magicians: 
    print(f"{magician.title()}, that's a great trick!")
    print(f"I cant wait to see your next trick,{magician.title()}.\n")
    print("Thank you, everyone. That was a great magic show!")

#------------------------------------------------------------
#task-pizza

pizzas=['cheese','veg','non-veg']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza.")
print("\nI really like cheese pizza.")
print("I generally prefer to add more cheese on my pizzas!")
print("I really love pizza!\n")

#task-animals

animals=['cat','dog','bird']
for animal in animals:
    print(f"A {animal.title()} would make a great pet!")
print("\nAny of these animal would make a great pet!")

#-------------------------------------------------------------

#making Numerical lists
#using the range() function - prints from 1 to 4

for value in range(1,5):
    print(value)
    
#prints from 1 to 5
for value in range(1,6):
    print(value)

#-------------------------------------------------------------

#using range() to make a list of numbers

numbers=list(range(1,6))
print(numbers)

#passing 3rd argument to range()
#3rd argument to add that specified number to the range

even_numbers=list(range(2,11,2))
print(even_numbers)

odd_numbers=list(range(1,11,2))
print(odd_numbers)

#square of numbers from 1 to 10
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

#To write the code more concisely, omit the variable,square
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

#simple statistics with a list of numbers
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#lit comprehension
squares=[value**2 for value in range(1,11)]
print(squares)

#-------------------------------------------------------------

#task-for loop - print 1 to 20 inclusive

for numbers in range(1,21):
    print(numbers)

numbers=list(range(1,1000001))
for numbers in range(1,1000001):
    print(numbers)

numbers=list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers=[]
for i in range(1,20,2):
    print(i)
    odd_numbers.append(i)
print(odd_numbers)

multiples_of_three=[]
for value in range(1,11):
    multiples_of_three.append(value*3)
print(multiples_of_three)

cubes=[]
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

#list comprehension
cubes=[value**3 for value in range(1,11)]
print(cubes)

#-------------------------------------------------------------

#working with part of a list
#slicing a list - working with specific group of items

#[0:3]- beginning till 2nd index i.e 3 values
#[1:4]-value of 1st index to 3rd index
#[:4]-beginning till 3rd index
#[2:]-2nd index till end
#[-3:]-last 3 players

players=['anu','keerthi','varun','ria','thara']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#Looping through a slice:
players=['anu','keerthi','varun','ria','thara']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
#copying a list - [:] copies the entrie list

my_foods=['dosa','poori','pongal','idli']
friend_foods=my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)

#append and check the output

my_foods.append('puttu')
friend_foods.append('idiyappam')
print(my_foods)
print(friend_foods)

#copying a list without slicing, simply setting equal to 
#this will make the changes in both the sets even we perform 
#any operation to one particular set
#both variables point to the same list

my_foods=['dosa','poori','pongal','idli']
friend_foods=my_foods
print(my_foods)
print(friend_foods)

my_foods.append('puttu')
friend_foods.append('idiyappam')
print(my_foods)
print(friend_foods)

#-------------------------------------------------------------

#task-using slice to print

players=['anu','keerthi','varun','ria','thara']
print("The first three players in the list are:")
print(players[0:3])
print("\nThree players from the middle of the list are:")
print(players[2:])
print("\nThe last three players in the list are:")
print(players[-3:])

#task-using slice to copy
my_fruits=['apple','orange','mango','kiwi']
friend_fruits=my_fruits[:]

print(my_fruits)
print("\n",friend_fruits)

my_fruits.append('avacodo')
friend_fruits.append('banana')

print("My favorite fruits are:")
for fruit in my_fruits:
    print("\n",fruit)

print("My friend's favorite fruits are")
for friend in friend_fruits:
    print("\n",friend)
    
#-------------------------------------------------------------

'''Copy a List'''

#You cannot copy a list simply by typing list2 = list1, 
#because: list2 will only be a reference to list1, and 
#changes made in list1 will automatically also be made in list2.

#one way is to use the built-in List method copy() 
#creates diff memory location to both the lists and changes made in
#one list will not affect other

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
print(id(thislist))
print(id(mylist))

#Another way to make a copy is to use the built-in method list().

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
print(id(thislist))
print(id(mylist))

#--------------------------------------------------------------

'''Join Two Lists
One of the easiest ways are by using the + operator'''

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Another way to join two lists is by appending all the items from list2 into list1, one by one:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Or you can use the extend() method

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#-------------------------------------------------------------

'''Nested lists - A nested list is a list that appears as an element in another list. In this list, the
three-eth element is a nested list'''

a = ["hello", 2.0, 5, [10, 20]]

#If we print list[3], we get [10, 20]. To extract an element from the nested list,
#we can proceed in two steps:

b = a[3]
print(b[0])
print(b[1])

#Or we can combine them:
    
print(a[3][0])
print(a[3][1])

for x in a:
    print(x)

#-----------------------------------------------------------

'''Matrices'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix[1]

matrix[1][1]

#-------------------------------------------------------------

'''String and lists'''

import string

song = "The rain in Spain..."
splitted_song = song.split()
print(splitted_song)

splitted_song = song.split('ai')
print(splitted_song)
#Notice that the delimiter doesn’t appear in the list.

#join function

lst = ["I", "love", "mangoes"]
result_str = " ".join(lst)
print(result_str)


#-------------------------------------------------------------





















