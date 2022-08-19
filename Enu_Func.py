"""
Enumerate() in Python
when dealing with iterators, we also get need to keep a count of iterations. Python eases the programmer's task by providing a built-in function enumerate() for this task.

Syntax: 
enumerate(iterable, start=0)

"""

lst  = ["google", "tesla", "amazone", "microsoft"]

i = 1
for item in lst:
  if i%2 != 0:
    print(f"should apply in {item} ")
    i +=1
"""
output:
should apply in google
"""


#using enumerate
for index, item in enumerate(lst):
  if index%2 ==0:
    print(f"should apply in {item} ")

"""
output:
should apply in google 
should apply in amazone 
"""

# Python program to illustrate
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
  
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
  
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
  
# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

"""
output:
[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]
"""

# Python program to illustrate
# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]
  
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)
  
# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print (count, ele)
  
# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)

"""
output:
(0, 'eat')
(1, 'sleep')
(2, 'repeat')
100 eat
101 sleep
102 repeat
0
eat
1
sleep
2
repeat
"""