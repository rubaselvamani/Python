'''

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

'''

#count() scans the entire list, so it is O(n).

nums = [2,2,1,1,1,2,2,2]
nums_set = set(nums)

n = len(nums)
maj = (n)//2
#print(maj)

for num in nums_set:
    if nums.count(num) > maj:
        print(num)

