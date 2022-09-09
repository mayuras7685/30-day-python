#set
#different order every time you use them
# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
Set = set([1, 2, 'Mayur', 4, 'you', 6, 'are'])
print("\nSet with the use of Mixed Values")
print(Set)
  
# Accessing element using
# for loop
print("\nElements of set: ")
for i in Set:
    print(i, end =" ")
print()
  
# Checking the element
# using in keyword
print("mayur" in Set)

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


#------------------------------Frozen set------------------------------
# Same as {"a", "b","c"}
normal_set = set(["a", "b","c"])
  
print("Normal Set")
print(normal_set)
  
# A frozen set
# Frozen sets are immutable objects\
# set can be modified at any time, elements of the frozen set remain the same after creation.

frozen_set = frozenset(["e", "f", "g"])
  
print("\nFrozen Set")
print(frozen_set)
  
# frozen_set.add("h")

