"""
filter()
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

syntax: filter(function, sequence)
function : function that test if each element of a sequance true or not
sequance : sequance which needs to be filterd(list, tuple, containers, sets)
"""
l1 = [1, 2, 3, 4, 5, 6, 7, 8]

def is_greater_4(l1):
  return l1>4

gr_than_4 = list(filter(is_greater_4, l1))
print(gr_than_4)

# output : [5, 6, 7, 8]