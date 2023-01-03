"""fibonaci"""
# n = int(input("Fibbonaci series"))

# def fibs(n):
#   if n<=1:
#     return n
#   else:
#     return (fibs(n-1)+fibs(n-2))


# if n<0:
#   print("Please enter positive integer")
# else:z
#   for i in range(n):
#     print(fibs(i))


"""patter printing"""

# n = int(input())

# for i in range(0, n):
#   for j in range(0, i+1):
#     print("x", end=" ")
#   print(" ")

"""function to convert sting into upper case and 
find length of string. string will be passed to function 
from main program print both the return value in main program 
"""
# def upLen(str):
#   return print("Upper case and length of str", str.upper(), len(str)) 

# upLen("my name is mayur")


"""class marks max, min, avg"""
# n = int(input("Students in class"))
# marks = []
# for i in range(n):
#   i = int(input(f'Enter Marks of studnt no. {i+1}'))
#   marks.append(i)

# #find avg. marks of class
# avg1 = sum(marks)/len(marks)

# #find max. marks of class
# max1 = max(marks)

# #find min. marks of class
# min1 = min(marks)

# print(marks)

# print(f'Avg. of class is: {avg1}')
# print(f'Max. marks of class is: {max1}')
# print(f'Min marks of class is: {min1}')

"""
Write a python program to read data from “file1.csv”, if data is
negative write it in “negative.csv” and if data is positive write it
in “positive.csv”
"""

# import csv

# with open("input.csv")as fobj:
#   heading = next(fobj)
#   reader = csv.reader(fobj)

#   for row in reader:
#     num = int(row[0])
#     if num>=0:
#       with open ("pos.csv") as file1:
#         writer1 = csv.writer(file1)
#         writer1.writerow(num)
#     else:
#       with open ("neg.csv") as file2:
#         writer2 = csv.writer(file2)
#         writer2.writerow(num)
#     file1.close()
#     file2.close()
# fobj.close()

"""convert string into list"""

# def strtolist(str):
#   return str.split()

# str1 = strtolist("My name is mayur")
# print(str1)

# print(type(str1))

"""display 0 to 100 even numbers"""

# for i in range(100):
#   if i%2==0:
#     print(i)
 
# while True:
#   n = int(input("Enter a interger"))
#   if n == 0:
#     break
#   print(str(n) + "*" + str(n) + "=" + str(n*n))
# print("done")


"""explain nested if 
to get temp to get temp and humidity from the user.
Display folloeing message in different situation
1. temp > 30 and humidity < 20% msg: Hot and Dry 
2. 30 < temp < 20 and 40% < humidity <20% msg: good weather condition
3. 30 < temp < 20 and humidity more than 80% msg: mositure present """

# t = int(input("Current Temp. in Celcuious ex. 23"))
# h = int(input("Humidity in percentage ex. 20"))

# if t>30 and h<20:
#   print("Hot and Dry")
# elif 20 < t < 30 and 20 < h < 40:
#   print("good weather condition") 
# elif 20 < t < 30 and h > 80:
#   print("Mostiure present")


""" wrp thst accepts a sentence and calculate the numbers of 
words
digit
uppercase letters 
lowercase letters
"""

# def count(str):
#   upper, lower, digit, space = 0, 0, 0, 0
#   words = str.split()
#   for i in range(len(str)):
#     if str[i].isupper():
#       upper += 1
#     elif str[i].isdigit():
#       digit += 1
#     elif str[i].islower():
#       lower += 1 
#     else:
#       space +=1
#   print("No. uppercase letters: ", upper)
#   print("No. lowercase letters :", lower)
#   print("No. of digit: ", digit)
#   print("No. of words in string: ", len(words))

# count("ABCD1234abcd")

"""wap to find the sum of all odd numbers up to a number specified by the user"""

# def oddsum(n):
#   sum = 0 
#   for i in range(n+1):
#     if i%2 == 1:
#       sum += i
#   print(sum)

# oddsum(5)


"""wap to get number from the userand find the sum of digits in entered number
by the user and print the sum of the digits in number"""

# def numsum(n):
#   sum = 0 
#   while n>0:
#     digit = n % 10
#     sum = sum + digit 
#     n //= 10
#   print(sum)

# numsum(12345)


"""find factorial of given number"""

# def factorial(n):
#   if n == 1:
#     return 1
#   else: 
#     return (n * factorial(n-1))

# print(factorial(10))

"""Given year leap year or not"""

# year = int(input("Enter year to cheack leap year or not"))

# def leapyear(year):
#   if year%4 == 0 and year%100 != 0:
#     print(f"{year} year is leap year")
#   elif year%400==0:
#     print(f"{year} year is leap year")
#   elif year%100==0:
#     print(f"{year} year is not leap year")
#   else:
#     print(f"{year} year is not leap year")

# leapyear(year)

"""
wap to input information for 5 number of students as given below:
a. Name
b. Registration number
c. Total Marks
"""

# s1 = []

# for i in range(5):
#   name = input("\nName: ")
#   reg = int(input("Registration number: "))
#   marks = int(input("Total marks: "))
#   s1.append(name)
#   s1.append(reg)
#   s1.append(marks)

# print(s1)

"""
wap to prompt for a marks in the rang of 0 to 100 if the entered marks is out 
of range, it should print an error, if the entered marks is between 0 and 100,
print grade using following information.
marks >= 70       A
60 <= marks < 70  B
50 <= marks < 60  C
40 <= marks < 50  D
marks <40         F
"""

# marks = int(input("Enter your marks"))

# if marks <= 100 :
#   if marks <40:
#     print("Your Grade is F")
#   elif marks >= 40 and marks < 50:
#     print("Your Grade is D")
#   elif marks >= 50 and marks < 60:
#     print("Your Grade is C")
#   elif marks >= 60 and marks < 70:
#     print("Your Grade is B")
#   elif marks >= 70  :
#     print("Your Grade is A")
# else:
#   print("Your Marks should be  0 to 100")

"""
wap to count the number of times an item appers in the list
"""

# def count(lst, x):
#   count = 0
#   for i in lst:
#     if i==x:
#       count += 1
#   return count

# lst1 = [1, 2, 3, 4, 2, 4, 3]

# print(count(lst1, 4))

"""
wap to find given points lies in which quandrant of x y plain 
print message of corresponding quandrant 
++ 1st q
-+ 2nd q
-- 3rd q
+- 4th q
"""

# def quad(x, y):
#   quad = "1st"
#   if x > 0 and y > 0:
#     quad = "1st"
#   elif x < 0 and y > 0:
#     quad = "2nd"
#   elif x < 0 and y < 0:
#     quad = "3rd"
#   else:
#     quad="4th"
#   return quad

# print(quad(2, -3))

"""
Write a Python program to check the validity of a password entered by
the user. Provide prompt to the use to enter the password.
The Password should satisfy the following criteria:
1. Contain at least 1 letter between a and z
2. Contain at least 1 number between 0 and 9
3. Contain at least 1 letter between A and Z
4. Minimum length of password: 6
If password satisfies all above condition, print message “Valid
password” else print message “Invalid password”
"""

# l, u, d = 0, 0, 0
# s = str(input('Enter your Password'))
# if (len(s) >= 6):
#     for i in s:
#         # counting lowercase alphabets
#         if (i.islower()):
#            l+=1           
#         # counting uppercase alphabets
#         if (i.isupper()):
#             u+=1           
#         # counting digits
#         if (i.isdigit()):
#             d+=1           
#         # counting the mentioned special characters
 
# if (l>=1 and u>=1 and d>=1 and l+u+d==len(s)):
#     print("Valid Password")
# else:
#     print("Invalid Password")