'''Python Inheritance

Parent class'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

'''child class'''

class Student(Person):
  pass

#use the Student class to create an object, and then execute the printname method'''
#The child's __init__() function overrides the inheritance of the parent's __init__() function.
x = Student("Mike", "Olsen")
x.printname()

#Add the __init__() Function
class Student(Person):
  def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname
  def printname(self):
      print(self.firstname, self.lastname)
      
x = Student("sindhu", "sudhakar")
x.printname()   

         
#To keep the inheritance of the parent's __init__() function, 
#add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)  
    
x = Person("John", "Doe")
x.printname()      

'''Use the super() Function - that will make the child class inherit all the 
methods and properties from its parent'''
   
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    

#Add properties
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)    
print(x.graduationyear)

#In the example below, the year 2019 should be a variable, 
#and passed into the Student class when creating student objects. 
#To do so, add another parameter in the __init__() function:
    
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

#Add methods:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    