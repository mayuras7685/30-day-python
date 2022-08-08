"""
for loop is used for iterating over a sequance

syntax:
for iterator_var in sequeance:
  -----statment-----

"""

#use string as sequance
str1 = 'i love india'
for a in str1:
  print(a)
"""
output:
i
 
l
o
v
e

i
n
d
i
a
"""

#use list as sequance
l1 = ['fruits', 'vegies', 'number', 3, 5, 45.5]
for b in l1:
  print(b)

"""
output:
fruits       
vegies       
number       
3
5
45.5
"""

#use tuple as sequance
t1 = (1 , 2, 4, 5, 6)
for c in t1:
  print(c)

"""
output:
1
2
4
5
6
"""

"""
range() function
for var in range(start, stop, increments)
  ----statmets----
!important 
loop excute till (stop - 1)

"""

for x in range(6):
  print(x)
"""
output:
0
1
2
3
4
5
"""