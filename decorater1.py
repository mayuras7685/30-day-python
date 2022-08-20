

def dec1(func1):
  def nowexecute():
    print("Executing Now")
    func1()
    print("Executed")
  return nowexecute

@dec1
def sample():
  print("Sample using dec")

sample()

"""
output:
Executing Now
Sample using dec
Executed
"""

import time
import math
"""
decorator to calculate duration
taken by any function.
""" 
def calculate_time(func):
     
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
 
        # storing time before function execution
        begin = time.time()
         
        func(*args, **kwargs)
 
        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
 
    return inner1
 
 
 
# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
 
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))
 
# calling the function.
factorial(10)

"""
output:
3628800
Total time taken in :  factorial 2.0089921951293945  
"""


#Chaining Decorators
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
 
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
 
@decor1
@decor
def num():
    return 10
 
print(num())
"""
output:
400

The above example is similar to calling the function as –

decor1(decor(num))
"""