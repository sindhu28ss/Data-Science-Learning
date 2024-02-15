# 1. defining classes

class Employee: # the class is named Employee

    # the first method is the __init__ method, we also call it constructor
    # because we are going to invoke this method to create employee instances
    # The first argument 'self' is the instance (the employee object) itself
    # we can call it other names, but it is better to stick to the convention
    # the rest of the arguments are used to pass in the attributes for each employee object
    def __init__(self,first,last,pay):
        self.first_name=first # "first_name" is the attribute name, "first" is the value passed in 
        self.last_name=last
        self.salary=pay
        self.email=first+'.'+last+'@company.com' # we can create attributes with known input values

emp1=Employee('xxx','yyy',50000)
emp2=Employee('sss','ttt',60000)

# access the object attributes using object_name.attribute_name
print(emp1.salary)
print(emp2.salary)
print(emp1.email)
print(emp2.email)


# ---------------------------------------------------------------------------------------------
# 2. creating method for objects

# create and access object method
class MyClass:

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()
MyClass.function(myobjectx)

# back to the employee class
class Employee:

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'

    def fullname(self):
        return '{}, {}'.format(self.last,self.first)
        # In '{}, {}'.format(self.last_name,self.first_name), the {} are place holders
        # and they will be filled with the arguments passed to the format function
        # the first {} will be filled with the first argument passed to the format function
        # the second {} will be filled with the second argument passed to the format function

emp1=Employee('xxx','yyy',50000)
print(emp1.fullname()) # invoke the fullname method to print out the fullname
# ---------------------------------------------------------------------------------------------
# 3. class variables

# call class variable for an object
class MyClass:
    variable = "class_variable"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable) # every created object from the class has the class-level variable as attribute
myobjectx.variable='what' # we can update attributes of objects outside the class as well.
print(myobjectx.variable)

# call class variable within class
class Employee:

    raise_amount=1.05 # this is the class variable
                      # we don't need to pass it into the class methods to use it
   
    def __init__(self,first,last,pay): 
        self.first_name=first
        self.last_name=last
        self.salary=pay
        self.email=first+'.'+last+'@company.com'

    def apply_raise(self): # no need to pass in raise_amount variable
        self.salary=int(self.salary*Employee.raise_amount) # you can call class variable like this

emp1=Employee('xxx','yyy',50000)
print(emp1.salary) # print out the salary before raise
emp1.apply_raise()
print(emp1.salary) # print out the salary after raise
# ---------------------------------------------------------------------------------------------
# 4. external variables

class Employee:
   
    def __init__(self,first,last,pay):
        self.first_name=first
        self.last_name=last
        self.salary=pay
        self.email=first+'.'+last+'@company.com'

    def bonus(self,firm_earning): # firm_earning is outside variable passed to the function when invoked
        self.bonus=firm_earning*0.05 # suppose the bonus is 5% of the firm earning.
                                                                # after this step, the employee will have another attribute "bonus"

emp1=Employee('xxx','yyy',50000)
emp1.bonus(10000) # invoke the bonus method and pass in the required outside variable
print(emp1.bonus) # print out the bonus attribute of the employee
# ---------------------------------------------------------------------------------------------
# 5. if you don't use __init__ method

# define the Vehicle class
class Vehicle:
    # define the default  attribute values for cars as class_level variable
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# define car objects
# As we don't have __init__ method, we have to define attributes one by one
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# call description method
print(car1.description())
print(car2.description())
# ---------------------------------------------------------------------------------------------
# 7. another example

import random
import string
#print(string.ascii_lowercase)
class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #  method 1
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    #  method 2
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    # this is a static method
    @staticmethod
    def naming(num_char):
        return ''.join(random.choices(string.ascii_lowercase,k=num_char))
	
# define dog objects
jake = Dog("Jake", 7)
doug = Dog("Doug", 4)
william = Dog("William", 5)

# Determine the oldest dog
def get_biggest_number(*args): # variable numbers of inputs
    return max(args)

print("The oldest dog is {} years old.".format(
    get_biggest_number(jake.age, doug.age, william.age)))

# call methods
print(jake.description())
print(jake.speak("Gruff Gruff"))

# call static method
print(Dog.naming(4))
# ---------------------------------------------------------------------------------------------
# 8. subclass

class Boss:
    
    boss_salary="high"
    
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face
    
class goodboss(Boss): # inherit all attributes, variables, and method from boss class 
    pass
    
boss1=Boss('x','negative','angry','hate')
print(boss1.get_attitude())
print(boss1.get_behaviour())

boss2=goodboss('y','positive','happy','smile')
print(boss2.get_face()) # inherit method
print(boss2.boss_salary) # inherit attributes
help(goodboss)


# create different class level variable in sub class
class Boss:
    
    boss_salary=100
    
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face
    
    def get_salary(self):
        return self.boss_salary
    
class goodboss(Boss): # inherit all attributes, variables, and method from boss class 
    boss_salary=200
    
boss1=goodboss('x','positive','happy','smile')
print(boss1.get_salary())
boss2=Boss('x','negative','angry','hate')
print(boss2.get_salary())


# create more attributes for the sub class
# suppose that the subclass good boss also has an additional attribute "howgood"

class Boss:

    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face
    
class goodboss(Boss): 
    
    def __init__(self, name, attitude, behaviour, face, howgood):
        super().__init__(name,attitude, behaviour, face) # pass these variables to the init method from the parent class, 
                                                         # and let that init method handle these attributes
        # you could also use Boss.__init__(self, name,attitude, behaviour, face)
        self.howgood=howgood # the extra attribute in the goodboss class
    
boss1=goodboss('y','positive','happy','smile','sweet')
print(boss1.howgood)
print(boss1.behaviour)
# in this way, we can take advantage of most of the codes in the parent class, and just add a little customization in the sub class.


# create customized method for the sub class
class Boss:

    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face
    
class goodboss(Boss): 
    
    def __init__(self, name, attitude, behaviour, face, howgood):
        super().__init__(name,attitude, behaviour, face) 
        self.howgood=howgood 
        
class badboss(Boss):
    def __init__(self, name, attitude, behaviour, face, howbad=None): # the default of howbad is None
        super().__init__(name,attitude, behaviour, face) 
        if howbad is None: # if the user refuse to tell you how bad the bad boss is, the howbad attribute is set to "nothing"
            self.howbad="nothing"
        else:
            self.howbad=howbad # if the user tells you how bad, then input this attribute
    
    def get_howbad(self): # we can add customized method for the sub class
        return self.howbad
    
boss1=badboss('y','negative','unhappy','hate','to the bone')
print(boss1.get_howbad())

boss1=badboss('y','negative','unhappy','hate')
print(boss1.get_howbad())

#try
boss2=goodboss('x','positive','nhappy','smile','managable')
print(boss2.howgood)

# ---------------------------------------------------------------------------------------------
# 9. a comprehensive example on subclass

class Employee:

    def __init__(self, name, attitude, behaviour):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
    
    def get_name(self):
        return self.name
    
class Senior(Employee): 
    
    def __init__(self, name, attitude, behaviour, ratings):
        super().__init__(name,attitude, behaviour) 
        self.ratings=ratings
        
class Boss(Employee):
    def __init__(self, name, attitude, behaviour, manage=None): # the manage attribute is a list, defining who the big boss is managing, the list will contain a list of smallboss objects
        super().__init__(name,attitude, behaviour) 
        if manage is None: # if the manage list is not provided, make this an empty list
            self.manage=[]
        else:
            self.manage=manage 
            
    def add_Emp(self,employee): 
        if employee not in self.manage:
            self.manage.append(employee)
        
    def drop_Emp(self,employee):
        if employee in self.manage:
            self.manage.remove(employee)
    
    def get_Emp(self):
        for i in self.manage:
            if i is not None:
                print(i.get_name())
    
senior_emp=Senior('x','positive','happy',100)
regular_emp=Employee('y','positive','unhappy')
boss=Boss('z','positive','happy',[senior_emp]) # remember that the manage attribute should be list

print(boss.get_name())
# let's add an employee to the manage
boss.get_Emp()
boss.add_Emp(regular_emp)
boss.get_Emp()
# let's drop an employee from the manage
boss.drop_Emp(senior_emp)
boss.get_Emp()

# ---------------------------------------------------------------------------------------------
# 10. multiple inheritance

class class1:
    def method1(self):
        return 1

class class2:
    def method2(self):
        return 2
    
class class3(class1,class2): 
    '''
	when inheriting from multiple classes,use comma to delimit them
	'''
    pass

x=class3()
print(x.method1())
print(x.method2())

# ---------------------------------------------------------------------------------------------
# 11. rules for method overide

# the class appearing first get priority
class class1:
    def method1(self):
        return 1

class class2(class1):
    def method1(self): # method overide
        return 2
    
class class3(class1):
    def method1(self): # method overide
        return 3

class class4(class2,class3):
    pass

x=class4()
print(x.method1()) # returns 2 since class2 appears first in the class4 definition.
    
# ---------------------------------------------------------------------------------------------
# 12. we can sometimes group multiple function calls into a class and run that class to get all function calls


class calculation:
    val = 3
    
    def step1(val):
        return float(val)+1
    
    def step2(val):
        return val**2
    
    def run():
        step1v = calculation.step1(calculation.val)
        step2v = calculation.step2(step1v)
        print(step2v)
        
if __name__=="__main__":
    calculation.run()
# ---------------------------------------------------------------------------------------------
# 13. more about static method

class MyClass:
    
    def method(x):
        print(x)

# work
MyClass.method(2) 
# does not work
obj = MyClass()
obj.method(2) # if an object is instantiated, you are actually passing two parameters
                # one is the obj itself, the other is 2
                # but the funciton method only takes one parameter

# the following works since the method does take 2 parameters.
class MyClass:
    
    def method(self,x):
        print(x)
         
obj = MyClass()
obj.method(2)


# the following works too since by adding the staticmethod decorator, the obj.method does not pass the self parameter.
class MyClass:
    @staticmethod 
    def method(x):
        print(x)

MyClass.method(2)        
obj = MyClass()
obj.method(2)

# ---------------------------------------------------------------------------------------------
# 14. calling class and class method from another script

# suppose in one script we have the following codes:

'''class c:
    
    def __init__(self,x):
        self.x = x
        
    def m(self,y):
        print(y)
        
    def s(t):
        print(t)
 '''       
        
# then we can access this class from other script by doing the following:

import script as s

s1 = s.c(2)
print(s1.x) # check the attribute x of l1
s1.m(6)
s.c.s(8)
s1.s(7) # wrong, it passes itself to the method s but the method s does take the self paramter


