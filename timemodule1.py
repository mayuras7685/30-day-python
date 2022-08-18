import time

initial1 = time.time()

i = 0

while(i<45):
  print(i)
  i +=1

print("While loop run in", time.time()-initial1, "Seconds")

initial2 = time.time()
for i in range(50):
  print(i)

print("For llop run in", time.time()-initial2, "Seconds")

"""
output:
1
.... 49
While loop run in 0.005002021789550781 Seconds 
1
.... 49
For llop run in 0.04500150680541992 Seconds
"""

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

# output : Thu Aug 18 21:38:07 2022