import copy
d1 = {}
d1['name']= 'Ram'
d1['age']= 'Sita'

print(d1)
d2= d1
print(d2) # shallow copy - Same object is referenced for d1 and d2
d3 = copy.deepcopy(d1) # deep copy - Different object is referenced for d1 and d3
d1['Place']= 'Ayodhya'
print(f'd1:{d1}, memory {id(d1)}')
print(f'd2 - Shallow copy:{d2}, memory {id(d2)}')
print(f'd3 - Deep copy:{d3}, memory {id(d3)}')
#memory address
print(id(d1))
print(id(d2))
print(id(d3))
print(d3.items())


d= {}
print(d.setdefault("city","NY"))
