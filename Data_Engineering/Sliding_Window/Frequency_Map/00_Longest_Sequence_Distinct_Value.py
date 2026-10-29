'''
Problem: Longest substring without repeating characters
Given a string of restaurant or event codes, find the length of the longest substring without repeated characters.
'''

#given_str = "abcabcbb"

given_str = "abcbdef"


seen = set()
left = 0
longest = 0

for right in range(len(given_str)):
     while given_str[right] in seen: # this could be in any order hence while instead of if
         seen.remove(given_str[left])
         left +=1 #adjust the initial position based on duplicate removal

     seen.add(given_str[right])
     longest = max(longest, right-left+1)

print(longest)



