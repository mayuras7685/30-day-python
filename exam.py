#fibonaci
n = int(input("Fibbonaci series"))

def fibs(n):
  if n<=1:
    return n
  else:
    return (fibs(n-1)+fibs(n-2))


if n<0:
  print("Please enter positive integer")
else:z
  for i in range(n):
    print(fibs(i))

# patter printing

n = int(input())

for i in range(0, n):
  for j in range(0, i+1):
    print("x", end=" ")
  print(" ")

"""function to convert sting into upper case and 
find length of string. string will be passed to function 
from main program print both the return value in main program 
"""
def upLen(str):
  return print("Upper case and length of str", str.upper(), len(str)) 

upLen("my name is mayur")



n = int(input("Students in class"))
marks = []
for i in range(n):
  i = int(input(f'Enter Marks of studnt no. {i+1}'))
  marks.append(i)

#find avg. marks of class
avg1 = sum(marks)/len(marks)

#find max. marks of class
max1 = max(marks)

#find min. marks of class
min1 = min(marks)

print(marks)

print(f'Avg. of class is: {avg1}')
print(f'Max. marks of class is: {max1}')
print(f'Min marks of class is: {min1}')

"""
Write a python program to read data from “file1.csv”, if data is
negative write it in “negative.csv” and if data is positive write it
in “positive.csv”
"""

import csv

with open("input.csv")as fobj:
  heading = next(fobj)
  reader = csv.reader(fobj)

  for row in reader:
    num = int(row[0])
    if num>=0:
      with open ("pos.csv") as file1:
        writer1 = csv.writer(file1)
        writer1.writerow(num)
    else:
      with open ("neg.csv") as file2:
        writer2 = csv.writer(file2)
        writer2.writerow(num)
    file1.close()
    file2.close()
fobj.close()