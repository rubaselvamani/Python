'''
This pattern is useful for time-series data, detecting changes, consecutive events, transaction changes, and timestamp gaps.
'''
values = [10, 15, 12, 20]

for previous, current in zip(values, values[1:]):
    print(previous, current)
