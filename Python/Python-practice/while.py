#Python has two primitive loop commands:
#while loops
#for loops

#The while Loop - we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1

#The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
#The break Statement - we can stop the loop even if the while condition is true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#The continue Statement - we can stop the current iteration, and continue with the next
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#The else Statement - we can run a block of code once when the condition no longer is true'''
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#Tables
import math
x = 1.0
while x < 10.0:
    print (x, "’\t’" , math.log(x))
    x = x + 1.0

str=['produces','this','output']
for x in str:
    print(x)
    for j in x:
        print("\t",j)
        
print("produces\n\t\tthis\n\n\t\t\t\toutput.")

#Two-dimensional tables'''
i = 1
while i <= 6:
    print(2*i,end=" ")
    i = i + 1
#print()

#Encapsulation and generalization'''
def printMultiples(n):
    i = 1
    while i <= 6:
        print(n*i, end=" ")
        i = i + 1
    print()

printMultiples(5)
printMultiples(3)
printMultiples(10)

