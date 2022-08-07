"""
Operators that Python Language supports are:

Arithmetic Operators
Assignment Operators
Comparison Operators
Logical Operators
Identity Operators
Membership Operators
Bitwise Operators
"""

# Arithmetic Operators
print("5 + 6 is ", 5+6)
print("5 - 6 is ", 5-6)
print("5 * 6 is ", 5*6)
print("5 / 6 is ", 5/6)
print("5 ** 3 is ", 5**3)
print("5 % 5 is ", 5%5)
print("15 // 6 is ", 15//6)


# Assignment Operators
print("Assignment Operators")
x = 5
print(x)
x %=7 
# x = x%7
print(x)

"""
== 
+=
-=
/=
%=
//=
**=
&=
|=
^=
>>=
<<=
"""


# Comparison Operators
i = 5
"""
== equal
!= not equal
> greater than
< less than
>= greater than or equal to
<= less than or equal to
"""


# Logical Operators
a = True
b = False
print(a and b) #False
"""
and
or 
not
"""


# Identity Operators
print(5 is not 3) #True
print(3 is 5) #False


# Membership Operators
l = [1, 2, 3, 5, 6]
print(4 in l) #False
print(4 not in l) #True


# Bitwise Operators
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

print(0 & 2) #0
print(0 | 3) #3

"""
& 
|
^
~
<<
>>
"""