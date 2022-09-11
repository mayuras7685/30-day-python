"""
Syntax of constructor declaration : 

def __init__(self):
    # body of the constructor

Constructors are generally used for instantiating an object.
1.default constructor: doesn’t accept any arguments
2.parameterized constructor: first argument as self and rest of argument provided by us
"""

# Example of default constructor: 
class GeekforGeeks:
 
    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"
 
    # a method for printing data members
    def print_Geek(self):
        print(self.geek)
 
 
# creating object of the class
obj = GeekforGeeks()
 
# calling the instance method using the object obj
obj.print_Geek()

#output: GeekforGeeks


#-------------------------------------------------------------------------------


# Example of parameterized constructor:
class Vgec:
 
    # Class Variable
    branch = 'ECE student'
 
    # The init method or constructor
    def __init__(self, name, div, batch):
 
        # Instance Variable
        self.name = name
        self.div = div
        self.batch = batch
    
    def print_details(self):
      return f"{self.name} is {self.branch} of {self.div} divison and batch of {self.batch} "
 
 
mayur = Vgec('Mayur', 'I', 'I1')

print(mayur.print_details())
#output: Mayur is ECE student of I divison and batch of I1 

print(mayur.batch)
#output: I1

