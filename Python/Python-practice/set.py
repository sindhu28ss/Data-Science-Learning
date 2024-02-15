#set
#Create a set

myset = {"apple", "banana", "cherry"}
print(myset) #Sets are unordered, so you cannot be sure in which order the items will appear.

#Duplicates Not Allowed - Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#The values True and 1 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#Get the Length of a Set

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#A set can contain different data types:

set1 = {"abc", 34, True, 40, "male"}
myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor - use the set() constructor to make a set.

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)    
    
#Access set items:

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)   
  
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)  
  
#Add Items

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)  
  
#Add Sets - To add items from another set into the current set, 
#use the update() method.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Add Any Iterable - The object in the update() method does not have to be a set, 
#it can be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#Remove Item - To remove an item in a set, 
#use the remove(), or the discard() method. 

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
 
#If the item to remove does not exist, remove() will raise an error.
  
thisset = {"apple", "cherry"}
thisset.remove("banana")
print(thisset) 
  
#You can also use the pop() method to remove an item, but this method will remove a random item, 
#so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.  

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)  
  
#clear() method:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
  
#The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset) #raises error 

#Loop Items:

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Join Two Sets - union() method:
#The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)   

#The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#NOTE: Both union() and update() will exclude any duplicate items.

#Keep ONLY the Duplicates
#The intersection_update() method will keep only the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#The intersection() method will return a new set, that only contains the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#Keep All, But NOT the Duplicates
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)




 
  
  
    