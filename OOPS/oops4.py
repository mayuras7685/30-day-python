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

class Base1(object):
    def __init__(self):
        self.str1 = "abc"
        print("Base1")
 
 
class Base2(object):
    def __init__(self):
        self.str2 = "xyz"
        print("Base2")
 
 
class Derived(Base1, Base2):
    def __init__(self):
 
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
 
    def printStrs(self):
        print(self.str1, self.str2)
 
 
ob = Derived()
ob.printStrs()

"""
output:
Base1
Base2
Derived
abc xyz
"""

