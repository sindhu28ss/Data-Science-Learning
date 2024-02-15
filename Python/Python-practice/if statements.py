#IF statements
#if
a = 33
b = 200
if b > a:
  print("b is greater than a")

#elif - if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else - The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#You can also have an else without the elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#Short Hand If - If you have only one statement to execute, 
#you can put it on the same line as the if statement'''
a=10
b=5
if a > b: print(a, "is greater than", b)

#Short Hand If ... Else - If you have only one statement to execute, 
#one for if, and one for else, you can put it all on the same line'''
a = 2
b = 330
print(a) if a > b else print(b)

#This technique is known as Ternary Operators, or Conditional Expressions.
#One line if else statement, with 3 conditions:
a = 350
b = 370
print(a) if a > b else print("=") if a == b else print(b)


#And - The and keyword is a logical operator, and is used to combine conditional statements
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


#Or - The or keyword is a logical operator, and is used to combine conditional statements
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


#Not - The not keyword is a logical operator, and is used to reverse the result of the conditional statement
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


#Nested If - You can have if statements inside if statements, 
#this is called nested if statements.
x = 11
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The pass Statement - if statements cannot be empty, 
#but if you for some reason have an if statement with no content, 
#put in the pass statement to avoid getting an error
a = 33
b = 200
if b > a:
  pass

#-------------------------------------------------

cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

#conditional statements-case sensitive
car='Audi'
car=='audi'
car.lower()=='audi'

#Inequality
selected_car='BMW'
if selected_car!='Audi':
    print("Hold the car!")

#Numerical comparison
age=18
age==18

#!=
answer=16
if answer!=42:
    print("That is not the correct answer. Please try again!")
    
#mathematical comparisons in conditional statements:
age=16
print(age<20)
print(age<=20)
print(age>20)
print(age>=20)

#-----------------------------------------------------------------------------

#checking multiple conditions
#using and to check multiple conditions
age_0=22
age_1=18
age_0>=21 and age_1>=21

#() improves readability
age_0=22
age_1=22
(age_0>=21) and (age_1>=21)

#using or to check multiple conditions
age_0=22
age_1=18
(age_0>=21) or (age_0>=21)

age_0=18
age_1=18
(age_0>=21) or (age_0>=21)

#-----------------------------------------------------------------------

#checking whether a value is in a list
cars=['audi','bmw','toyota','honda']
print('audi' in cars)
print('Audi' in cars) #case sensitive
print('subaru' in cars)

#checking whether a value is not in a list
cars=['audi','bmw','toyota','honda']
car='subaru'
if car not in cars:
    print(f"{car.title()}, is not in the list")
    
#Boolean expression
game_active=True
can_edit=False

#----------------------------------------------------------------------

#task-conditional tests

fruit='apple'
fruit=='apple'
fruit=='mango'
fruit='ORANGE'
print(fruit.lower())


value_0=12
value_1=20
value_0>=10 and value_1<=25
value_0>=10 and value_1<=15
value_0>=10 or value_1<=19
value_0>=15 or value_1<=19

fruits=['apple','orange','mango','banana']
fruit='apple'
if fruit in fruits:
    print(f"{fruit.title()} is available")
fruit='kiwi'
if fruit not in fruits:
    print(f"{fruit.title()} is not available")

#------------------------------------------------------------

#if-else statements:
    
age=int(input("Please enter your age:"))
if age>=18:
    print("You are old enough to vote!")
    print("Have you registered for vote yet?")
else:
    print("sorry, you are too young to vote.")
    print("Please register to vote as you turn 18!")
    
#if-elif-else statements:

age=int(input("Please enter your age: "))
if age<4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
    
#print statement outside the if-else block:
    
age=int(input("Please enter your age: "))
if age<4:
    price=0
elif age<18:
    price=25
else:
    price=40
print(f"Your admission cost is ${price}")

#Multiple elif blocks:
age=int(input("Please enter your age: "))
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
else:
    price=20
print(f"Your admission cost is ${price}")

#Omitting the else block
age=int(input("Please enter your age: "))
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
elif age>=65:
    price=20
print(f"Your admission cost is ${price}")

#-------------------------------------------------------------
    
#Testing multiple conditions:

requested_toppings=['extra cheese','grilled chicken']
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
if 'olives' in requested_toppings:
    print("Adding olives")
if 'grilled chicken' in requested_toppings:
    print("Adding grilled chicken")
print("\n Finished making your pizza!")

#-------------------------------------------------------------

#task- multiple if statements
alien_color='green'
if alien_color=='green':
    print("The player just earned five points!")
if alien_color=='yellow':
    print("The player doesnt won any point")
    
#task- if-else blocks    
alien_color='green'
if alien_color=='green':
    print("The player just earned five points!")
else:
    print("The player just earned ten points!")
    
alien_color='yellow'
if alien_color=='green':
    print("The player just earned five points!")
else:
    print("The player just earned ten points!")
    
#task-if-elif-else blocks
alien_color='green'
if alien_color=='green':
    print("The player just earned 5 points!")
elif alien_color=='yellow':
    print("The player just earned 10 points!")
else:
    print("The player just earned 15 points!")
    
alien_color='yellow'
if alien_color=='green':
    print("The player just earned 5 points!")
elif alien_color=='yellow':
    print("The player just earned 10 points!")
else:
    print("The player just earned 15 points!")
    
alien_color='red'
if alien_color=='green':
    print("The player just earned 5 points!")
elif alien_color=='yellow':
    print("The player just earned 10 points!")
else:
    print("The player just earned 15 points!")

#task- if-elif-else
age=int(input("Please enter the age:"))
if age<2:
    print("The person is a baby")
elif age==2 or age<4:
    print("The person is a toddler")
elif age==4 or age<13:
    print("The person is a kid")
elif age==13 or age<20:
    print("The person is a teenager")
elif age==20 or age<65:
    print("The person is an adult.")
else:
    print("The person is older.")
    
#list-if statements
favorite_fruits=['Apple','Orange','Mango']
if 'Mango' in favorite_fruits:
    print("I really love Mango")
if 'Orange' in favorite_fruits:
    print("Orange is one of my favorite_fruit")
if 'banana' in favorite_fruits:
    print("Banana is not in the list")
if 'kiwi' in favorite_fruits:
    print("Kiwi is not in the list")
if 'Apple' in favorite_fruits:
    print("Apple is in the list")
    
 #-----------------------------------------------------------

#using if statements with lists:
requested_toppings=['mushroom','extra cheese','olives']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your Pizza!")

#checking for special items:
requested_toppings=['mushroom','extra cheese','olives']
for requested_topping in requested_toppings:
    if requested_topping=='olives':
        print("sorry, we are out of Olives right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your Pizza!")


#checking that a list is not empty:
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your Pizza!")
else:
    print("Are you sure you want a plain pizza?")

#using Multiple lists:
available_toppings=['mushrooms','olives','green peppers','pepperoni',
                    'pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"sorry, we dont have {requested_topping}.")
print("\nFinished making your pizza!")

#------------------------------------------------------------
#task-Hello Admin

users=['sindhu','sudhakar','thara','admin','nandini']
for user in users:
    if user=='admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, Thank you for logging in again.")
        
#no users:
users=[]
if users:
    for user in users:
        if user=='admin':
            print("Hello Admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, Thank you for logging in again.")
else:
    print("we need to find some users!")
    
#checking usernames:
current_users=['sindhu','sudhakar','thara','admin','nandini']
new_users=['sindhu','sudhakar','ria','anu','preethi']
for new_user in new_users:
    if new_user in current_users:
        print("Please enter a new username.")
    else:
        print("The username is available.")
        
#ordinal numbers:
numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number==1:
        print(f"{number}st")
    elif number==2:
        print(f"{number}nd")
    elif number==3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
        
#-------------------------------------------------------------
    
    



    





































