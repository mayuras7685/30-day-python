"""
Inheritance:
one class to derive or inherit the properties from another class

Inheritance syntax:

Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}

Different types of Inheritance:
Single inheritance: child class inherits from only one parent class
Multiple inheritance: child class inherits from multiple parent class 

"""

# Single inheritance
class Baseclass(object):
  def __init__(self, name):
    self.name = name
  
  def getname(self):
    return self.name

  def isBaseclass(self):
    return False

class DerivedClass(Baseclass):
  def isBaseclass(self):
    return True

  
   
cls1 = Baseclass("Mayur")
print(cls1.getname(), cls1.isBaseclass())

cls1 = DerivedClass("Not Mayur")
print(cls1.getname(), cls1.isBaseclass())

"""
output:
Mayur False
Not Mayur True
"""

# Multiple inheritances

