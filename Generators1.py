"""
Iterable=__iter__() or __getitem__()
Iterator=__next__()
Iteration=this process
"""

def gen(n):
    for i in range(n):
        yield i

# for i in range(5):
#     print(i)

g=gen(5)
print(g)
print(g.__next__())
print(g.__next__())

for i in g:
    print(i)

m="mayur"
ier=iter(m)
print(ier.__next__())
for c in m:
    print(c)


