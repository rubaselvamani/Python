'''
Peak server resource usage
'''

jobs = [
    (1, 5, 10),   # start, end, GB
    (2, 6, 20),
    (4, 8, 15)
]

memory_use = []

for start,end,memory in jobs:
    memory_use.append((start,memory))
    memory_use.append((end, -memory))

memory_use.sort()
print(memory_use)

current_memory =0
peak_memory = 0

for i in range(len(memory_use)-1):
    time,memory_change = memory_use[i]
    current_memory += memory_change

    next_time = memory_use[i+1] [0]
    if current_memory > peak_memory:
        peak_memory = current_memory
        peak_interval = (time,next_time)

print(peak_memory,peak_interval,type(peak_interval))

