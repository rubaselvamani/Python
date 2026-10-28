'''
Problem: Longest sequence with at most K cancellations
Find the longest consecutive order sequence containing at most k cancellations.
'''

orders = [1, 1, 0, 0, 1, 1, 1, 0]
k = 2

left = 0
best = 0
cancellation = 0


for right in range(len(orders)):

    if orders[right] == 0:
        cancellation +=1

    while cancellation > k :
        if orders[left] == 0:
            cancellation -=1
        left += 1

    best = max(best,right-left+1)

print(best)

