'''Tuples'''

#Create Tuple With One Item
#To create a tuple with only one item, you have to add a comma after the item, 
#otherwise Python will not recognize it as a tuple.'''

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

#The tuple() Constructor -  to make a tuple.

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#Change Tuple Values - Convert the tuple into a list to be able to change it'''   

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Add Items - Convert into a list: Just like the workaround for changing a tuple, 
#you can convert it into a list, add your item(s), 
#and convert it back into a tuple'''

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#Add tuple to a tuple - if you want to add one item, (or many), create a new tuple with the item(s), 
#and add it to the existing tuple:'''

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#Remove Items - Convert the tuple into a list, remove "apple", 
#and convert it back into a tuple'''

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Unpacking a Tuple

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#NOTE: The number of variables must match the number of values in the tuple, 
#if not, you must use an asterisk to collect the remaining values as a list.

#Using Asterisk*
#If the number of variables is less than the number of values, 
#you can add an * to the variable name 
#and the values will be assigned to the variable as a list'''

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Join Two Tuples - you can use the + operator'''

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


#Multiply Tuples - you can use the * operator'''

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#-------------------------------------------------------------------------------

dimensions=(200, 50)
print(dimensions[0])
print(dimensions[1])

#trying to assign a new value to tuple
dimensions[0]=250

#Looping through all values of a tuple
dimensions=(200,50)
for dimension in dimensions:
    print(dimension)
    
#writing over a tuple
dimensions=(200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions=(400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    
#-----------------------------------------------------------------------------

foods=('caribbean','vietnamese','korean','german','indian')
for food in foods:
    print(food)
#food[0]='Thai'
#print(foods)
foods=('Thai','French','Indian','Mexican','Korean')
print("\nThe new set of cuisine:")
for food in foods:
    print(food)
    
#-----------------------------------------------------------------------------













    
    
    