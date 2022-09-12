"""
Destructors:
Destructors are called when an object gets destroyed.
but in python destructors are not needed as much as in C++ because Python has a garbage collector that handles memory management automatically. 

Syntax of destructor declaration : 

def __del__(self):
  # body of destructor

"""

class Employee:
 
    # Initializing
    def __init__(self):
        print('Employee created.')
 
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')
 
obj = Employee()
del obj

"""
output:
Employee created.
Destructor called, Employee deleted.
"""

"""
he destructor was called after the program ended or when all the references to object are deleted
"""
class Employee:
 
    # Initializing
    def __init__(self):
        print('Employee created')
 
    # Calling destructor
    def __del__(self):
        print("Destructor called")
 
def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj
 
print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

"""
Output: 
Calling Create_obj() function...
Making Object...
Employee created
function end...
Program End...
Destructor called
""" 

class A:
    def __init__(self, bb):
        self.b = bb
 
class B:
    def __init__(self):
        self.a = A(self)
    def __del__(self):
        print("die")
 
def fun():
    b = B()
 
fun()

#output: die

"""
Note:
if your instances are involved in circular references they will live in memory for as long as the application run.
"""