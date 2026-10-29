'''
Maximum concurrent data-pipeline jobs
'''

pipelines = [
    ("ETL_A", 1, 8),
    ("ETL_B", 2, 5),
    ("ETL_C", 4, 7),
    ("ETL_D", 6, 10)
]

etl_jobs = []
for etl_job,start,end in pipelines:
    etl_jobs.append((start,1,etl_job))
    etl_jobs.append((end,-1,etl_job))

etl_jobs.sort()
print(etl_jobs)

current = 0
max_concurrent = 0
max_concurrent_time = []
active_jobs = []

for start,change,etl_job in etl_jobs:
    current += change
    max_concurrent = max(max_concurrent,current)

#print(max_concurrent)

max_etl_jobs_interval = {}
current = 0
for i in range(len(etl_jobs)-1):
    start,change,etl_job = etl_jobs[i]
    next_time = etl_jobs[i+1][0]
    current += change
    if change == 1:
        active_jobs.append(etl_job)
    else:
        active_jobs.remove(etl_job)

    if current == max_concurrent:
        #print(active_jobs)
        max_etl_jobs_interval[(start,next_time)] = active_jobs.copy()

print(max_etl_jobs_interval)
