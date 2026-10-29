'''
Number of active sessions at each timestamp
'''

sessions_1 = [
    (1, 5),
    (2, 7),
    (4, 6)
]

sessions = [
    (1, 5),
    (2, 5),
    (5, 8)
]

events = []

for start,end in sessions:
    events.append((start,1))
    events.append((end, -1))

events.sort()
print(events)
active_sessions = {} # set is created to avoid time overlap
current = 0

for time,change in events:
    current += change
    active_sessions[time] = current

print(active_sessions)
