'''
Problem: Find the 'longest consecutive order sequence' containing "at most" 2 cancellations.
'''

#orders = [1, 1, 0, 0, 1, 1, 1, 0]
#orders = [0, 0, 0, 1, 1, 1, 1]
#orders = [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
orders = [0,0,0,0]
k = 2



longest_sequence = 0
cancellation = 0
left = 0

for right in range(len(orders)):
    if orders[right] == 0:
        cancellation +=1

    while cancellation > k:
        if orders[left] == 0:
            cancellation -=1
        left +=1

    longest_sequence = max(longest_sequence, right-left +1)

print(longest_sequence)

