'''
Problem: Minimum consecutive orders to reach a revenue target
Given positive order amounts, find the minimum number of consecutive orders whose total revenue is at least target.
'''


amounts = [2, 3, 1, 2, 4, 3]
target = 7

current = 0
best = float('inf')
left = 0

for right in range(len(amounts)):
    current += amounts[right]

    while current >= target:
        best = min(best, right - left + 1)
        current -= amounts[left]
        left +=1



print(best)


