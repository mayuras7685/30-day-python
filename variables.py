"""
variables naming rules:
variable name must start with a letter or the underscore character
variable names are case-sensitive

camel case:
myVariableName 

Pascal case:
MyVariableName

Snake case:
my_variable_name

"""
var1 = "string"
var2 = 10
var3 = 23.5

print(type(var1))
print(type(var2))
print(type(var3))

#print(var1 + var2)#this statement throws error beacuse of string and interger not concatenate


#typecasting

a = 2
b = 3
c = '8'
d = '5'

print(a+b)#5
print(int(c)+int(d))#13
print(str(a)+str(b))#23
