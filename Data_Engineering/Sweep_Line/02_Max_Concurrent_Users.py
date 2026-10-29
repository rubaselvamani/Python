'''
Maximum concurrent users
'''

sessions = [
    ("u1", 1, 5),
    ("u2", 2, 8),
    ("u3", 4, 6),
    ("u4", 7, 10)
]

events = []
for user,start,end in sessions:
    events.append((start,1,user))
    events.append(( end, -1,user))

events.sort()
print(events)

current = 0
max_u = 0
for time,event,user in events:
    current += event
    max_u = max(current, max_u)

print(max_u)
