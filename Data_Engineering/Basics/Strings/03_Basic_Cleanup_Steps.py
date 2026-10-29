
##################1. Basic String Cleaning####################

#Remove unwanted whitespace (or characters):

text = "  hello world  "
print(text.strip())      # "hello world"
print(text.lstrip())     # "hello world  "
print(text.rstrip())     # "  hello world"


#Standardize text case:
text = "Data Science"
print(text.lower())   # "data science"
print(text.upper())   # "DATA SCIENCE"
print(text.title())   # "Data Science"



##################2. Searching & Matching####################

#Locate substrings:
text = "apple banana"
print(text.find("banana"))   # 6
#text.index("carrot")# throws error


#Binary return
print(text.startswith("app"))   # True
print(text.endswith("na"))      # True
#print(text.contains("na"))      # no such function

##################3. Splitting & Joining####################
#join()
#Break strings into lists:
data = "A,B,C"
data.split(",")   # ['A', 'B', 'C']


#join()
#Combine lists into strings:
",".join(['A', 'B', 'C'])   # "A,B,C"



##################4. Replacing & Modifying####################
#replace()
text = "I like cats"
text.replace("cats", "dogs")   # "I like dogs"


##################5. Checking String Content####################

#Useful for validation:
"abc".isalpha()    # True
"123".isdigit()    # True
"abc123".isalnum() # True

##################6. Advanced Text Handling####################
#splitlines()
text = "line1\nline2\n"
print("Split lines: ", text.splitlines())   # ['line1', 'line2']

#partition()
#Splits into 3 parts:
text = "key xyz =value xyz="
print('partition: ', text.partition("="))

##################7. Useful in Data Analysis (with Pandas)####################
# When working with datasets, these are commonly used via pandas:
import pandas as pd
'''
df['col'].str.lower()
df['col'].str.strip()
df['col'].str.contains("apple")
df['col'].str.replace("old", "new")
df['col'].str.split(",")

'''

##################8. Regular Expressions (Very Important)####################

import re

text = "Order ID: 12345"
print(re.findall(r"\d+", text))   # ['12345']

