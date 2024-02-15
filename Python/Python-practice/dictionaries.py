#Dictionary
#Create and print a dictionary:
    
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Dictionaries cannot have two items with the same key:
#Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Dictionary Length:
print(len(thisdict))

#Dictionary Items - can be of any data type:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))

#The dict() Constructor - to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Accessing Items
#You can access the items of a dictionary by referring to its key name, inside square brackets:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#There is also a method called get() that will give you the same result:

x = thisdict.get("model")
print(x)
print(thisdict.get("model"))

#Get Keys:
#The keys() method will return a list of all the keys in the dictionary.

print(thisdict.keys())

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#Get Values
#The values() method will return a list of all the values in the dictionary.

x = thisdict.values()
print(x)
print(thisdict.values())

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#Get Items
#The items() method will return each item in a dictionary, as tuples in a list.

x = thisdict.items()
print(x)
print(thisdict.items())

#Check if Key Exists
#To determine if a specified key is present in a dictionary use the in keyword:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Change Values
#You can change the value of a specific item by referring to its key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

#Update Dictionary
#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

#-----------------------------------------------------------

#Removing Items
#The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)   

#The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#The del keyword can also delete the dictionary completely:
    
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.

#The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#------------------------------------------------------------

#Loop Through a Dictionary - for loop
#Print all key names in the dictionary, one by one:
    
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
  
#You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)

#------------------------------------------------------------

#Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])
  
#You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)   

#-----------------------------------------------------------

#Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)

#------------------------------------------------------------

#Copy a Dictionary - You cannot copy a dictionary simply by typing dict2 = dict1, 
#because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

print(id(thisdict))
print(id(mydict))

#Another way to make a copy is to use the built-in function dict().

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#-----------------------------------------------------------

#Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Or, if you want to add three dictionaries into a new dictionary:

child1 = {
  "name" : "kiki",
  "year" : 2004
}
child2 = {
  "name" : "jyo",
  "year" : 2007
}
child3 = {
  "name" : "ria",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Access Items in Nested Dictionaries
#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary

print(myfamily["child2"]["name"])

#-----------------------------------------------------------

value={'color':'green','points':5}
print(value['color'])
print(value['points'])

#Accessing values in a dictionary
value={'color':'green','points':5}
newpoints=value['points']
print(f"You have earned {newpoints} points!")
print(f"You have earned {value['points']} points!")

#Adding new key-value pairs: x_position & y_position
value={'color':'green','points':5}
print(value)
value['x_position']=0
value['y_position']=25
value['speed']='medium'
print(value)

#starting with an empty dictionary
value={}
value['color']='green'
value['points']=5
print(value)

#Modifying values in a dictionary
value={'color':'green','points':5}
print(f"The color is {value['color'].title()}.")
value['color']='yellow'
print(f"The color now is {value['color'].title()}.")

value={'x':0,'y_position':25,'speed':'medium'}
print(f"original position: {value['x']}.")
if value['speed']=='slow':
    x_increment=1
elif value['speed']=='medium':
    x_increment=2
else:
    x_increment=3
value['x']=value['x']+x_increment
print(f"New position: {value['x']}.")

#Removing key-value pairs:
value={'color':'green','points':5}
print(value)
del value['points']
print(value)

#A Dictionary of similar objects
favorite_languages={
    'sindhu':'python',
    'sudhakar':'python',
    'thara':'java',
    'ria':'c',
    }
print(f"Sindhu's favorite language is {favorite_languages['sindhu'].title()}.")

#using get() to access values
value={'color':'green','points':5}
#print(value['speed']) #gives keyerror
speed_value=value.get('speed','No speed value assigned')
#'No speed value assigned' or juz 'none' is fine
print(speed_value)

#------------------------------------------------------------------

#task-person

person={'first_name':'Sindhuja','last_name':'Arivukkarasu',
        'age':25,'city':'chennai'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#favorite_nos
favorite_numbers={'sudhakar':1,'sindhu':2,
                  'thara':3,'ria':4,'anu':5}
print(f"Sudhakar's favorite_number is {favorite_numbers['sudhakar']}.")
print(f"Sindhu's favorite_number is {favorite_numbers['sindhu']}.")
print(f"Thara's favorite_number is {favorite_numbers['thara']}.")
print(f"Ria's favorite_number is {favorite_numbers['ria']}.")
print(f"Anu's favorite_number is {favorite_numbers['anu']}.")

#----------------------------------------------------------

#Looping through a dictionary
#for k,v in dictionary.items()

user_0={'username':'asindhuj',
        'first':'Sindhuja',
        'last':'Arivukkarasu',}
for key,value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages={
    'sindhu':'python',
    'sudhakar':'python',
    'thara':'java',
    'ria':'c',
    }
for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#Looping through all the keys in a dictionary - keys()
favorite_languages={
    'sindhu':'python',
    'sudhakar':'python',
    'thara':'java',
    'ria':'c',
    }
for name in favorite_languages.keys():
    print(name.title())

#for name in favorite_languages.keys():
#for name in favorite_languages:
#both gives the same output
favorite_languages={
    'sindhu':'python',
    'sudhakar':'python',
    'thara':'java',
    'ria':'c',
    }
for name in favorite_languages:
    print(name.title())
#
favorite_languages={
    'sindhu':'python',
    'sudhakar':'python',
    'thara':'java',
    'ria':'c',
    }
friends=['sindhu','sudhakar']
for name in favorite_languages.keys():
    print(f"Hi,{name.title()}.")
    if name in friends:
        language=favorite_languages[name].title()
        print(language)
        print(f"{name.title()}, I see you love {language}.")
    
#not in 
favorite_languages={
    'sindhu':'python',
    'sudhakar':'python',
    'thara':'java',
    'ria':'c',
    }
if 'sindhuja' not in favorite_languages.keys():
    print("Sindhuja, Please take our poll!")

#Looping through a dictionary's keys in a particular order:
#sorted() - sort that list before looping through it
favorite_languages={
    'sindhu':'python',
    'sudhakar':'python',
    'thara':'java',
    'ria':'c',
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#Looping through all values in a dictionary:
#values()

favorite_languages={
    'sindhu':'python',
    'sudhakar':'python',
    'thara':'java',
    'ria':'c',
    }  
print("\nThese are the languages mentioned.") 
for language in favorite_languages.values():
    print(language.title())
    
#set - gives only unique items in a list

favorite_languages={
    'sindhu':'python',
    'sudhakar':'python',
    'thara':'java',
    'ria':'c',
    }  
print("\nThese are the languages mentioned.") 
for language in set(favorite_languages.values()):
    print(language.title())
    
#sample set - stores only unique values,unordered
language={'Python','C','Java','Python'}
print(language)

#------------------------------------------------------------
#task-rivers
famous_rivers={'India':'Ganges',
        'United States':'Yellowstone',
        'Egypt':'Nile'}
for country,river in famous_rivers.items():
    print(f"The {river.title()} runs through the {country.title()}.")
print("\nList of rivers:")   
for river in famous_rivers.values():
    print(river.title())
print("\nList of countries:")
for country in famous_rivers.keys():
    print(country.title())
    
#------------------------------------------------------------


    























   



    