"""
Example of txt file:

--------mayur.txt--------
My name is mayur.
I am student of ECE.
-------------------------

"""

# tell() function : to know where is file pointer

f = open("mayur.txt")
print(f.tell()) # output: 0
print(f.readline())
print(f.tell()) #output : 16
print(f.readline())
print(f.tell()) #output : 36

# seek() : to reset file pointer

f = open("mayur.txt")
print(f.tell()) # output: 0
print(f.readline())
f.seek(0) # reset file pointer to 0
print(f.tell()) #output : 16
print(f.readline())