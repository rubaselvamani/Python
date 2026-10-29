
'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

'''
Time:  O(n)
Space: O(n)
'''
nums = [9,6,4,2,3,5,7,0,1]
nums_set = set(nums)
for i in range(1,len(nums)+1):
     if i not in nums_set:
         print(i)
