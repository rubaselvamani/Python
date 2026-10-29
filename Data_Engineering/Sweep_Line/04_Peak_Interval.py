'''
Return the peak interval
'''

meetings = [(1, 5), (2, 7), (4, 6)]
event = []
for start,end in meetings:
    event.append((start,1))
    event.append((end,-1))

event.sort()
print(event)
print(len(event))

current = 0
max_m = 0
peak_interval = None # initialize Because peak_interval assignment is conditional:

for i in range(len(event)-1):
    start_time, change = event[i]
    current += change
    next_time = event[i+1][0] if i+1 < len(event) else None
    if current > max_m:
        max_m = current
        peak_interval= (start_time,next_time)

print(f"{max_m=},{peak_interval=}")



