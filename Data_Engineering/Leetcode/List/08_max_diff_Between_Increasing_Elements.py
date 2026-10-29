'''
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.


'''

nums= [7,1,5,4]
max_diff = 0

for i in range(1,len(nums)):
    diff =  nums[i] - nums[i-1]

    max_diff = max(max_diff,diff)

if max_diff >0:
    print(max_diff)

else:
    print(-1)
