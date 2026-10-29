'''

Maximum consecutive orders without cancellation
Given 1 for a completed order and 0 for a canceled order, find the longest consecutive sequence of completed orders.

'''

orders = [1, 1, 0, 1, 1, 1, 0, 1]
best = 0

# counter approach
sequence = 0
for right in range(len(orders)):
    if orders[right] == 0:
        sequence = 0

    else:
        sequence += 1
        best = max( best, sequence)

print("Method 1: ", best)

#algorithmic approach
left = 0
best = 0
for right in range(len(orders)):
    if orders[right] == 0:
        left = right+1

    else:
        best = max(best,(right-left)+1)
        #print(right,left)
        #print(best)
print("Method 2: ", best)








