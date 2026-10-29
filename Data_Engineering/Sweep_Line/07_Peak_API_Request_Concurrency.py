'''
Peak API request concurrency
'''

requests = [
    ("r1", 1, 4),
    ("r2", 2, 6),
    ("r3", 3, 5),
    ("r4", 7, 9)
]

request_cnt = []

for request,start,end in requests:
    request_cnt.append((start,1))
    request_cnt.append((end,-1))

request_cnt.sort()
print(request_cnt)

#### Approach 1
current = 0
peak_request = 0
peak_interval = None


for i in range(len(request_cnt)-1):

    time,change = request_cnt[i]
    current += change
    next_time = request_cnt[i+1][0]

    if current > peak_request:
        peak_request = current
        peak_interval = (time,next_time)

print(peak_request,peak_interval)

#### Approach 2

current = 0
peak_request = 0
peak_interval = None


for i,(time,change) in enumerate(request_cnt):
    current += change


    if current > peak_request:
        peak_request = current
        next_time = request_cnt[i + 1][0] if i+1 < len(request_cnt) else None
        peak_interval = (time,next_time)

print(peak_request,peak_interval)
