'''
SQl equivalent:
Select user, event_cnt
from
(
select
user,count(distinct event)
from
user_event_tble
group by 1
order by 2 desc
)a
limit 3
'''

## In Python ##
events = [
    "u1", "u2", "u1", "u3",
    "u1", "u2", "u4", "u2"
]

user_events_cnt = {}

# Step 1: Aggregate the events
for user in events:
    user_events_cnt[user] = user_events_cnt.get(user,0)+1

print(user_events_cnt)

# Step 2: Sort the events
sorted_events = sorted(user_events_cnt.items(), key= lambda x: x[1], reverse = True)
print(sorted_events)

# Step 3: Top K users
k = 3

print(sorted_events[:k])

#output: [('u1', 3), ('u2', 3), ('u3', 1)]




