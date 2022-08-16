"""
Example of txt file:

--------mayur.txt--------
My name is mayur.
I am student of ECE.
-------------------------

"""


f = open("mayur.txt", "w")
f.write("Mayur full moj ma")
f.close()

#if file does not exiest then write mode create file
#write mode cleans file and write

#to append in file
f = open("mayur.txt", "a")
f.write("Add this line in file\n")
f.close()

#to open file in both read and write mode
f = open("mayur.txt", "r+")
print(f.read())
f.write("Thank you")