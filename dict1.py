#Dictionary is key value pairs
a = {'key': 'value', 'cow':'mooh'}
print(a['cow'])#prints moooh

#create a dict with each item as pair
Dict1 = dict([(1, 'Gimi'), (2, 'Fri')])
print("\nDictionary with each item as a pair: ")
print(Dict1)
#Dictionary with each item as a pair: 
#{1: 'Geeks', 2: 'For'}


#Add elements in dict
Dict2 = {}

Dict2[0] = "Mayur"
Dict2[2] = "Mohit"
Dict2[3] = "Samir"
#output : {0: 'Mayur', 2: 'Mohit', 3: 'Samir'}

#access a element of dict
print(Dict2['Mohit'])
#output :  2

#same for key

#some dict methods

dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
  
# copy() method
dict2 = dict1.copy()
print(dict2)
#output : {1: 'Python', 2: 'Java', 3: 'Ruby', 4: 'Scala'}
  
# clear() method
dict1.clear()
print(dict1)
#output : {}
  
# get() method
print(dict2.get(1))
#output : Python
  
# items() method
print(dict2.items())
#output : dict_items([(1, 'Python'), (2, 'Java'), (3, 'Ruby'), (4, 'Scala')])

# keys() method
print(dict2.keys())
#output : dict_keys([1, 2, 3, 4])
 
# pop() method
dict2.pop(4)
print(dict2)
#output : {1: 'Python', 2: 'Java', 3: 'Ruby'}
  
# popitem() method
dict2.popitem()
print(dict2)
#output : {1: 'Python', 2: 'Java'}

# update() method
dict2.update({3: "Scala"})
print(dict2)
#output : {1: 'Python', 2: 'Java', 3: 'Scala'}

# values() method
print(dict2.values())
#output : dict_values(['Python', 'Java', 'Scala'])
