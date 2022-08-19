l1 = ["Mayur", "Deep", "Mohit", "Samir", "Dev", "Zeel"]

for i in l1:
  print(i, "and", end=" ")

print("Are my chaddi buddy.")
"""
output:
Mayur and Deep and Mohit and Samir and Dev and Zeel and Are my chaddi buddy
"""

l2 = ["indra", "krishal", "dev", "raju", "vasu", "akshit"]

a = ", ".join(l2)
print(a, "are my college friends.")
"""
output:
indra, krishal, dev, raju, vasu, akshit are my college friends
"""