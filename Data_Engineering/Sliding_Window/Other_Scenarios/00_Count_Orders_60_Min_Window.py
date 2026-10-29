'''

Problem 9: Count orders in the last 60 minutes
Given sorted order timestamps in minutes, return the maximum number of orders within any 60-minute window.

'''

timestamps = [1, 10, 20, 50, 61, 70, 80]

left = 0
max_order = 0


for right in range(len(timestamps)):

    while timestamps[right] - timestamps[left] > 60:

        left +=1

    max_order = max(max_order, right - left + 1)

print(max_order)

###### Approach 2

timestamps = [1, 10, 20, 50, 61, 70, 80]

left = 0
max_order = 0

for right in range(len(timestamps)):

    while timestamps[right] - timestamps[left] > 60:
        left += 1

    max_order = max(max_order, right - left + 1)

print(max_order)
