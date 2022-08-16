# Python File IO Basics
"""
"r"- open file for reading - default
"w"- open file for writing - default
"x"- creates file if not exists
"a"- add more conntent to a file
"t"- text mode
"b"- binary mode
"+"- read and write

f = open(filename, mode)
"""
# to open file in read mode
f= open("file.txt", "r")
f.read()
f.close()

# to open file in write mode 
"""
also write mode create file if it does not exists """
file=open("Mayur.txt","w")
f.write("1234566788")
f.close()

# to append in file 
f=open("Mayur.txt","a")
f.write("mayur is python devloper\n")
f.close()

#handle read and write both
f=("Mayur1.txt","r+")
content=f.read()
print(content)
f.close()


