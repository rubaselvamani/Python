timestamps = [1, 5, 10, 50, 55]

for previous, current in zip(timestamps, timestamps[1:]):
    gap = current - previous

    if gap > 30:
        print("Large gap:", previous, current)
