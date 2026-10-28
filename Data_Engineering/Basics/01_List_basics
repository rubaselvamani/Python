################ Creation: ######################
print("*******Creation of lists*******")
numbers = [1, 2, 3, 4]
names = ["Alice", "Bob", "Charlie"]
names_1 = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 3.14, True]


empty_list = []
print(f"numbers: {numbers}")
print(f"numbers empty: {numbers[0]}")
print(f"names: {names},{id(names)}")
print(f"names_1: {names_1},{id(names_1)}")
print(f"mixed: {mixed}")
print(f"empty_list: {empty_list}")

print("*******Creation of lists ends here*******\n")

## Accessing Elements ###
numbers = [10, 20, 30, 40]
print("*******Accessing List Elements*******")
print(numbers[0])   # 10
print(numbers[-1])  # 40 (last element)
print("*******Accessing List Elements ends here*******\n")

############# Slicing ###############

numbers[1:3]   # [20, 30]
numbers[:2]    # [10, 20]
numbers[::2]   # [10, 30]  It returns every second element from the list.

print("*******List Slicing*******")

print(numbers[1:3])
print(numbers[:2])
print(numbers[::2],"\n")

print("*******List Slicing ends here*******\n")

'''
Common List Operations
1️⃣ Add Elements
'''

print("*******Add Elements*******")
print(f"numbers: {numbers}")
numbers.append(50)
print(f"numbers: {numbers}")
numbers.insert(1, 15)
print(f"numbers: {numbers}")
numbers.extend([60, 70])
print(f"numbers: {numbers}")
print("*******Add elements ends here*******\n")

### 2️⃣ Remove Elements

print("*******Remove elements*******")
print(f"numbers: {numbers}")
numbers.remove(20)   # removes value
print(f"numbers: {numbers}")
numbers.pop()        # removes last
print(f"numbers: {numbers}")
numbers.pop(1)       # removes by index
print(f"numbers: {numbers}")
print("*******Remove elements ends here*******\n")

### 3️⃣ Update Elements

print("*******Update elements*******")
numbers[0] = 100
print(f"numbers: {numbers}")
print("*******Update elements ends here*******\n")

### 3️⃣ Useful Built-in Functions

print("*******Built-in Functions*******")
print(f"len of numbers:{len(numbers)}")
print(f"min of numbers:{min(numbers)}")
print(f"max of numbers:{max(numbers)}")
print(f"sum of numbers:{sum(numbers)}")
print(f"sorted numbers:{sorted(numbers)}")
print("*******Built-in Functions ends here*******\n")



##🔹 List Comprehension (Very Important)
## Compact way to create lists
print("*******List Comprehension*******")
squares = [x*x for x in range(5)]
# [0, 1, 4, 9, 16]
print(f"squares:{squares}")


### With condition

evens = [x for x in range(10) if x % 2 == 0]
print(f"evens:{evens}")

print("*******List Comprehension ends here*******\n")
