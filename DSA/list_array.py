# Creating a List with
# the use of multiple values
List = ["Mayur", "For", "DSA"]
print("\nList containing multiple values: ")
print(List)
  
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List2 = [['mayur', 'For'], ['DSA']]
print("\nMulti-Dimensional List: ")
print(List2)
  

"""
   -8  -7  -6  -5  -4  -3  -2  -1   negetive index                             
  [01, 34, 95, 34, 42, 12, 36, 56]
    0   1   2   3   4   5   6   7   Positive index

"""  
# accessing a element from the
# list using index number
print("Accessing element from the list")
print(List[0])
print(List[2])
  
# accessing a element using
# negative indexing
print("Accessing element using negative indexing")
      
# print the last element of list
print(List[-1])
      
# print the third last element of list
print(List[-3])

l2 = [26, 2, 55, 6, 1, 23, 45]

#list slicing 
print(l2[:]) #[26, 2, 55, 6, 1, 23, 45]

print(l2[0:5]) #[26, 2, 55, 6, 1]

print(l2[-1]) #45

#extanded slicing 
print(l2[0::2]) #[26, 55, 1, 45]

print(l2[::-1]) #[45, 23, 1, 6, 55, 2, 26]