"""
Recursion
Recursion is a common mathematical and programming concept. 
It means that a function calls itself. This has the benefit of 
meaning that you can loop through data to reach a result.
"""
n = int(input())
m = int(input())
def fac1(n):
  if n == 1:
    return 1
  else:
    return n*fac1(n-1)

print("Factorial using recursion", fac1(n))
# output: Factorial using recursion 120


def fib(m):
  if m == 1:
    return 0
  elif m == 2:
    return 1
  else:
    return fib(m-1)+fib(m-2)

print("Fibonacci using recursion", fib(m))
"""
8
8
Factorial using recursion 40320
Fibonacci using recursion 13
"""