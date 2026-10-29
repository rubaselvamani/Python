'''
Find when peak concurrency occurred - return the time at which it occurred:
'''

meetings = [(1, 5), (2, 7), (4, 6)]
event = []
for start,end in meetings:
    event.append((start,1))
    event.append((end, -1))

event.sort()
print(event)

current = 0
max_m = 0
peak_time = None
for time,event in event:
    current += event
    max_m = max(max_m,current)
    if current == max_m:
        peak_time = time

print(f"{max_m=},{peak_time=}")



