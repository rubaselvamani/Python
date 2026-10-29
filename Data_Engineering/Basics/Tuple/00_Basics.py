
print ("Swapping Tuples:",end ="" )
x, y = 5, 10
print(f"{x=},{y=}")
x, y = y, x
print(f"{x=},{y=}")
print("creating Tuple")
t= 1,2,3
print(t,type(t),t[0],t[-1])



s = 5,
print(s,type(s))

t = (5,10)
x,y = t
print(x,y)
x,y = y,x
print(y)

print(t.count(5), t.index(5))

list = [1,2,3]
tup = tuple(list)
print(tup)

t = (1, 2, 2, 3, 4, 4, 5)

new_tuple = tuple(set(t))
print(new_tuple)

tuple = 1,[1,2]
print(type(tuple))
tuple[1][0] = 10

tuple = (1,2,3,4,5)
a,*rest,b = tuple
print(a,b,rest,type(rest),type(a))


tuple = (1,5)
a,*rest,b = tuple
print(a,b,rest,type(rest),type(a))

