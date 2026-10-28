'''
Maximum people in meetings — weighted intervals
'''

meetings = [
    (1, 5, 10),
    (2, 6, 20),
    (4, 7, 15)
]

events =[]
for start,end,people in meetings:
    events.append((start,1,people))
    events.append((end, -1, -people))

events.sort()
print(events)

current = 0
max_people = 0

for time,events,people in events:
    current += people
    max_people = max(current,max_people)
    #print(max_people)

print(max_people)
