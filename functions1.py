"""
Python Functions is a block of statements that return the specific task.

def function_name(parameters):
  -----statement-----
  return expression

return is optional 
but for further use of function you must define return value 
"""
#create firts function
def fun():
  print('welcome to fun')

#call the function
fun()
# output: welcome to fun



def add(num1, num2) -> int:
    """Add two numbers"""
    num3 = int(num1) + int(num2)
 
    return num3
 

ans = add(1, 4)
print(ans)
# output:5

"""
Docstring
The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function.
"""

def evenOdd(x):
    """Function to check if the number is even or odd"""
     
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

# print out the docstring of a function
print(evenOdd.__doc__)
# output: Function to check if the number is even or odd