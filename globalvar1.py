#Global Variable and global keyword

p = 17 #Global var.
def function1(n):
  p = 10 #local var.
  q = 12
  print(p, q)
  print(n, "function1 printed")

function1("Hi")
# output : 10 12 Hi function1 printed

"""function always cheacks first local var. and use it 
and when local var. not exiest then global var. was use 
Local ---> Global
"""

# l = 10

# def function2(n):
#   m = 12
#   l = l + 45
#   print(l, m)

# function2(4)
"""
Error :
line 22, in function2    l = l + 45
UnboundLocalError: local variabl
"""
#We not change global variable in function 
#we use global key word to change global variable

# also sglobal keyword use for To create a global variable inside a function
def myfunc(n):
  global x
  x = "fantastic"
  print(x, n)

myfunc(4)
print("Python is " + x)
# output : fantastic 4 , Python is fantastic


