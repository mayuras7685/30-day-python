"""
Example of txt file:

--------mayur.txt--------
My name is mayur.
I am student of ECE.
-------------------------

"""
# !important please close file after read or write
f = open("mayur.txt")
con = f.read()
print(con)
f.close()

"""
output: 
My name is mayur.
I am student of ECE.
"""

con1 = f.read(5)
print(con1)
# output: My na
con1 = f.read(5)
# output: me is
f.close()

# readline function
print(f.readline())
# output: My name is mayur.

#readlines function
print(f.readlines())
# output: ['My name is mayur.\n', 'I am student of ECE.']
