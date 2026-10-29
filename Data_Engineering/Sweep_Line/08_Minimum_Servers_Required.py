'''
Minimum number of servers required
This looks like a different problem, but:

minimum servers required = maximum number of overlapping jobs.
Each job occupies one server for its entire execution:
'''

jobs = [
    (1, 5),
    (2, 7),
    (4, 6),
    (8, 10)
]
job_run = []

for start,end in jobs:
    job_run.append((start,1))
    job_run.append((end,-1))

job_run.sort()
print(job_run)

current = 0
max_overlap = 0

for time,change in job_run:
    current += change
    if current > max_overlap:
        max_overlap = current

print(max_overlap)
