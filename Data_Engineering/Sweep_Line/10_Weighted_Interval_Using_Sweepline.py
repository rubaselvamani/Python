

meetings = [
    (1, 5, 10),
    (2, 6, 20),
    (4, 7, 15)
]

events = []

for start, end, weight in meetings:
    events.append((start, weight))
    events.append((end, -weight))

events.sort()

current_weight = 0
max_weight = 0
peak_interval = None

i = 0

while i < len(events):
    time = events[i][0]

    # Group events with identical timestamps
    while i < len(events) and events[i][0] == time:
        current_weight += events[i][1]
        i += 1

    if i < len(events):
        next_time = events[i][0]

        if current_weight > max_weight:
            max_weight = current_weight
            peak_interval = (time, next_time)

print(max_weight, peak_interval)
