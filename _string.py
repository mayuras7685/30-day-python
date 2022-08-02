#every instructions apply to all code in order
str1 = "My name is mayur"

print(type(str1))

#to find length of string
print(len(str1))#16

#string slicing

"""
                  -7 -6 -5 -4 -3 -2 -1                                   
M y    n a m e   i s     m  a  y  u  r
0 1 2  3 4 5 6 7 8 9  10 11 12 13 14 15
"""
print(str1[0:16]) #My name is mayur

print(str1[::])#My name is mayur

print(str1[0::])#My name is mayur

print(str1[::1])#My name is mayur

print(str1[:16:])#My name is mayur

#advance string slicing

print(str1[0:16:2])#M aei au

print(str1[-1:-7:-1])#ruyam

print(str1[::-1])#ruyam si eman yM


#various string functions

print(str1.endswith("Mayur"))#False

print(str1.count('a'))#2

print(str1.capitalize())#My name is mayur

print(str1.upper())#MY NAME IS MAYUR

print(str1.lower())#my name is mayur

print(str1.find("Mayur"))#-1

print(str1.replace("mayur", "Mohit"))#My name is Mohit

print(str1.isalnum())#False

print(str1.isalpha())#False

str2 = '123456789'

print(str2.isnumeric())#True

print("mayur" in str1)#True

print("mohit" not in str1)#True
