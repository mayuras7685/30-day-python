# stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. 
#insert --> push
# delete --> pop 

stack = []
  
# append() function to push
# element in the stack
stack.append('m')
stack.append('a')
stack.append('y')
stack.append('u')
stack.append('r')

  
print('Initial stack')
print(stack)

"""output: 
Initial stack
['m', 'a', 'y', 'u', 'r']  
"""
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop()) 
print(stack.pop())
print(stack.pop())

"""
output:
Elements popped from stack:
r
u
y
"""

  
print('\nStack after elements are popped:')
print(stack)

"""
output:
Stack after elements are popped:
['m', 'a']
"""

