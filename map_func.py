"""
map() function
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

syntax: map(fun, iter) 
fun = fuction that passes each element of iterable 
iter = it is iterable which is to be mapped like list, tuple, dict.

"""


num = ['2', '4', '54', '65', '45']

for i in range(len(num)):
  num[i] = int(num[i])

num[2] = num[2] + 1

print(num[2])
# output : 55

print(num)
# output: [2, 4, 55, 65, 45]

num = list(map(int, num))

print(num)
# output: [2, 4, 55, 65, 45]



squre = list(map(lambda x: x*x, num))
print(squre)
# output : [4, 16, 3025, 4225, 2025]


