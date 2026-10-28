'''
There are many meetings with start and end time. How many meetings can occur at the same time?
'''

#logic : Intervals → start/end events → sort events → sweep through them → maintain a running count.


#meetings = [(1, 5), (2, 7), (4, 6)]

meetings = [(1, 2), (2, 3), (3, 4)]

events = []

for start,end in meetings:
    events.append((start,1))
    events.append((end,-1))

print(events)
events.sort() #in place sorting
print(events)

#Max events - meetings
current_meetings = 0
max_meetings = 0

for meeting,event in events:
    current_meetings += event
    max_meetings = max(current_meetings,max_meetings)

print(f"{max_meetings=}")


