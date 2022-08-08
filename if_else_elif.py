"""
if (condition):
  -------------if block-------------
else:
- if condition true then if block excute
- if if condtion not excute then else excute

"""

# to find biggest number 


var1 = int(input())#12
var2 = int(input())#13
var3 = int(input())#14

if var1>var2 and var1>var3:
  print(f"{var1} is biggest number")
elif var2>var1 and var2>var3:
  print(f"{var2} is biggest number")
else:
  print(f"{var3} is biggest number")
# output : 14 is biggest number 


#if use in list
l1 = [1, 3, 4, 5, 6]
if 5 in l1:
  print(True)
else:
  print(False)

# output : True

#if use string
str1 = 'I love india'
if 'India' not in str1:
  print(True)
# output : True


#to find whether you drive or not
print("enter your age:")
age=int(input())
if age>18:
    print("you can drive")
elif age==18:
    print("wait for desison")
else:
  print("you can not drive")



