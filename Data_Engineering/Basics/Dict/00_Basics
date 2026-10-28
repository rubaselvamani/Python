

dict_1 = {'key_1': 1, 'key_2': 2}
print (dict_1.keys())
print (type(dict_1.keys()))
print (dict_1.values())
print (type(dict_1.values()))


student = {"name": "alice", "city": "london"}

upper_student = {k: v.upper() for k, v in student.items()}
print(upper_student)

original = {"a": 1, "b": 2, "c": 3}

swapped = {v: k for k, v in original.items()}
print(swapped)

numbers = {x: "even" if x % 2 == 0 else "odd" for x in range(1, 6)}
print(numbers)


d = {"a": 1}
if "a" in d.values():
    print("Exists")

d1 = {"a": 1}
d2 = {"b": 2}

print( f'New Concept: {d1|d2}')
print({**d1, **d2})


print (type(d.items()))
print(dict(d.items()))

d3 = {}
d3['name'] = 'Ram'
d3['age'] = '40'
print(d3)

print(f'place: {d3.get('place',0)}')
#print(f'place: {d3['place']}')

dict_1 = {'X1': "game 1", 'Level': 0}
dict_2 = {'X1': "game 3", 'Level': 1}
dict_3 = {'X1': "game 1"}
consolidate_dict = [dict_1,dict_2,dict_3]
print(consolidate_dict)
for dict_list in consolidate_dict:
    #print (dict_list)
    #print(dict_list.keys())
    #print(dict_list['Level'])
    print(dict_list.get('Level',0))
