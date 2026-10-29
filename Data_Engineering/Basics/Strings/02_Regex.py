import re

text = "My number is 123 123"
match = re.search(r"\d+", text)
print(match)

if match:
    print(match.group())  # 12345

text_x = "Hello World"
result = re.match(r"Hello", text_x)
print(result.group())


match_1 = re.search(r"\d",text)
print(match_1.group())


match = re.search(r"Order (\d+)", "Order 123 Sales 125")
print(match.group(1))   # '123'

match = re.search(r"Order (\d+)", "Order 123 Sales 125")
print(match.group())   # 'Order 123'

match = re.search(r"(\d+)", "Order 123 Sales 125")
print(match.group())   # '123'

match = re.findall(r"Order (\d+)", "Order 123 Sales 125")
print(match)   # '123'

match = re.findall(r"(\d+)", "Order 123 Sales 125")
print(match)   # '123 125'


print(re.findall(r"\w+@\w+\.\w+", "test@gmail.com"))
