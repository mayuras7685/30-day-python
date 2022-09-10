#class and object 

#class def


class ClassName:
    pass
    # Statement

#obj def
obj = ClassName()
print(obj.atrr)

# declaring an object 
class student:
 
    # A simple class
    # attribute
    attr1 = "mayur"
    attr2 = "m.d asodara"
 
    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
 
 
# Driver code
# Object instantiation
unkil = student()
 
# Accessing class attributes
# and method through objects
print(unkil.attr1)
unkil.fun()

"""
output:
mammal
I'm a mayur
I'm a m.d asodara
"""

"""
self:
we have a method that takes no arguments, we still have one argument,
We do not give a value for this parameter when we call the method, Python provides it.
  
__init__ method:
similar to constructors
collection of statements that are executed at the time of Object creation.
"""

# Sample class with init method
class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
p = Person('Nikhil')
p.say_hi()

#output: Hello, my name is Nikhil

"""
Instance variable:
are for data, unique to each instance and class variables are for attributes and methods shared by all instances of the class.
"""


class Vgec:
 
    # Class Variable
    branch = 'ECE student'
 
    # The init method or constructor
    def __init__(self, div, batch):
 
        # Instance Variable
        self.div = div
        self.batch = batch
 
 
# Objects of Vgec class
Mayur = Vgec("I", "I1")
Smit = Vgec("J", "J1")
 
print('Mayur details:')
print('Mayur is a', Mayur.branch)
print('Divison: ', Mayur.div)
print('Batch: ', Mayur.batch)
 
print('Smit details:')
print('Smit is a', Smit.branch)
print('Divison: ', Smit.div)
print('Batch: ', Smit.batch)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Vgec.branch)

"""
output:
Mayur details
Mayur is a ECE student 
Divison: I
Batch: I1

Smit details
Smit is a ECE student 
Divison: J
Batch: J1

Accessing class variable using class name
ECE student
"""