"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

n1= input()
n2 =input()

try:
  print("sum of n1 and n2", int(n1)+int(n2))

except Exception as e:
  print(e)

print("This line is very impotant!")

# n1 = 2, n2 = rw, output : invalid literal for int() with base 10: ''       This line is very impotant!


try:
  print(x)
except:
  print("An exception occurred")

#The try block will generate an exception, because x is not defined:


# More than one exception 
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
# output : Variable x is not defined



#The try block does not raise any errors, so the else block is executed:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# output : Hello Nothing went wrong


#The finally block gets executed no matter if the try block raises any errors or not:

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
# output :  Something went wrong The 'try except' is finished