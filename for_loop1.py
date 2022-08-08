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

#Increment the sequence with 3 (default is 1):
for y in range(2, 30, 3):
  print(y)
"""
output:
2
5
8
11
14
17
20
23
26
29
"""

#else in for loop
for z in range(6):
  print(z)
else:
  print("Finally finished!")

"""
output:
0
1
2
3
4
5
Finally finished!
"""

#Nested loops

#genrate ipl team names using nested for loop
city = ["ahmedabad", "mumbai", "kolkata", "pune"]
team_name = ["titans", "indians", "knight rider", "super giants"]

for p in city:
  for q in team_name:
    print(p, q)
"""
output:
ahmedabad titans
ahmedabad indians
ahmedabad knight rider
ahmedabad super giants
mumbai titans
mumbai indians
mumbai knight rider
mumbai super giants
kolkata titans
kolkata indians
kolkata knight rider
kolkata super giants
pune titans
pune indians
pune knight rider
pune super giants
"""
