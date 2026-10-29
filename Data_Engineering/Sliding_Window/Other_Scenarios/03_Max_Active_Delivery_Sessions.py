'''
Problem: Maximum active delivery sessions
Given delivery start and end times, find the maximum number of deliveries happening simultaneously.
'''


deliveries = [(1, 5), (2, 7), (4, 6), (8, 10)]


#sweepline
schedule = []

for start,end in deliveries:
    schedule.append((start,1))
    schedule.append((end, -1))


schedule.sort()


current = 0
best = current

for time,order in schedule:
    current +=order

    best = max(best,current)

print(best)


