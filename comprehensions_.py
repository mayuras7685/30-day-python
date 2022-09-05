"""LIST COMPREHENSIONS"""
#long metod
# ls=[]
# for i in range(10):
#     if i%3==0:
#         ls.append(i)


#comprehensions method
ls = [i for i in range(10) if i%3==0]
print(ls)


"""DICT. COMPREHENSIONS"""
#long method
# dict1={0:"item0",1:"item1",......}

#sort method
dict1={i:f"item{i}" for i in range(1,10)}
dict2={value:key for key,value in dict1.items()}
print(dict1,"\n",dict2)


"""SET COMPREHENSIONS"""
dresses={dress for dress in {"dress1","dress2","dress3","dress2","dress3"}}
print(dresses)


"""GENERATORS COMPREHENSIONS"""

evens=(i for i in range(100) if i%2==0)
print(evens.__next__())
print(evens.__next__())

for item in evens:
    print(item)
