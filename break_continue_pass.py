"""
break Statement
With the break statement we can stop the loop before it has looped through all the items
"""
#break in while loop
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
"""
output:
1
2
3
"""

#break in for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

"""
output:
apple
banana
"""


"""
continue Statement
With the continue statement we can stop the current iteration of the loop, and continue with the next
"""

#continue in while loop
j = 0
while j < 6:
  j += 1
  if j == 3:
    continue
  print(j)
"""
output:
1
2
3
4
5
6
"""

#continue in for loop
names = ["mayur", "deep", "viraj", "mohit"]
for n in names:
  if n == "viraj":
    continue
  print(n)

"""
output:
mayur        
deep
mohit 
"""

#Pass statement create a placeholder for future code
for h in (0, 5, 2):
  pass

#no output 