# mutable - list
# immutable - tuple



tup = (1, 2, 3)
print(tup)

#we not change tuple values


#Create Tuple with one item
tup2 = (1,)

#Tuple items are ordered, unchangeable, and allow duplicate values.

#Concatenation of Tuples in Python
t1 = (1, 3, 6)
t2 = ("Mayur", "Mohit", "Samir")

print(t1+t2)#(1, 3, 6, 'Mayur', 'Mohit', 'Samir')

#slicing tuples is also same as list and string 

#nested tuple
t3 = (t1, t2)
print(t3)#((1, 3, 6), ('Mayur', 'Mohit', 'Samir'))