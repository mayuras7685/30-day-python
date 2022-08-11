set1 = {"Mayur", "Mohit", "Viraj"}
print(set1)
# output: {'Viraj', 'Mohit', 'Mayur'}
# 2nd time we run this code {'Viraj', 'Mayur', 'Mohit'}

"""
the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
"""

# Duplicates not allowed : Sets cannot have two items with the same value.
set2 = {2, 3, 4, 2, 5, 6, 3}
print(set2)
# output: {2, 3, 4, 5, 6}

#length of a set
print(len(set2))
# output: 5

#Using the set() constructor to make a set

l1 = [2, 3, 4, 5, 2, 4]
l2 = set(l1)
print(type(l2)) #<class 'set'>
print(l2) #{2, 3, 4, 5}