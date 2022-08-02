#every instructions apply to all code in order
l1 = [2, 3, 4, "Mayur", "ram", 5]

print(l1) #[2, 3, 4, 'Mayur', 'ram', 5]

#to access list particular data
print(l1[2]) #4

#l1 is example of mixed list 

l2 = [26, 2, 55, 6, 1, 23, 45]

#list slicing 
print(l2[:]) #[26, 2, 55, 6, 1, 23, 45]

print(l2[0:5]) #[26, 2, 55, 6, 1]

print(l2[-1]) #45

#extanded slicing 
print(l2[0::2]) #[26, 55, 1, 45]

print(l2[::-1]) #[45, 23, 1, 6, 55, 2, 26]

#don't use minus slicing more then -1 

print(l2[0:7:-3]) #[]


#various list fuctions and methods 

l3 = [12, 2, 45, 3, 1, 67]

#to add data in list 
l3.append(23)
print(l3) #[12, 2, 45, 3, 1, 67, 23]

#to arrange disanding order 
l3.sort()
print(l3) #[1, 2, 3, 12, 23, 45, 67]

#to reverse list 
l3.reverse()
print(l3) #[67, 45, 23, 12, 3, 2, 1]

#to remove item from list 
l3.remove(12)
print(l3) #[67, 45, 23, 3, 2, 1] removed 12 

#to find particular items count
print(l3.count(12)) #0

#to insert items in list at particular index
l3.insert(3,3)
print(l3) #[67, 45, 23, 3, 3, 2, 1]

#to del digit of list 
l3.pop()
print(l3) #[67, 45, 23, 3, 3, 2]



