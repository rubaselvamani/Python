'''
Problem: Detect suspicious customer order activity
Flag customers who place at least k orders within a rolling 60-minute window.
'''

orders = [
    ("U1", 10),
    ("U1", 20),
    ("U2", 30),
    ("U1", 40),
    ("U2", 90)
]

k = 3
order_freq = {}


for user,timestamp in orders:
    order_freq.setdefault(user,[]).append(timestamp)


suspicious = set()

for user,timestamp_1 in order_freq.items():

    timestamp_1.sort()
    left = 0

    for right in range(len(timestamp_1)):
        while timestamp_1[right] - timestamp_1[left] > 60:
            left +=1


        if right-left +1 >= k:
            suspicious.add(user)
            break

print(suspicious)







