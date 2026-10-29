'''
Maximum orders in K minutes
Given the number of orders received each minute, find the maximum number of orders in any consecutive k minutes.

Select
start_minute
,sum(orders) partition by( rows between current row and K rows)
'''

orders = [10, 20, 15, 30, 25, 10]
k = 3

if k <= 0 or k > len(orders):
    max_order =  0

window_sum = sum(orders[:k])
max_sum = window_sum
#print(len(orders))

for right in range(k,len(orders)):
    #print(right)
    window_sum += orders[right]
    window_sum -= orders[right - k]
    max_sum = max(max_sum, window_sum)

print(f"Max Order: {max_sum}")
