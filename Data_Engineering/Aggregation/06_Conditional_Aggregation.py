
'''
expected_output =
{
 'u1': {'clicks': 2, 'purchases': 1},
 'u2': {'clicks': 1, 'purchases': 1}
}

SQL equivalent:

SUM(CASE WHEN event = 'click' THEN 1 ELSE 0 END)
'''

## In Python ##
events = [
    ("u1", "click"),
    ("u1", "purchase"),
    ("u1", "click"),
    ("u2", "purchase"),
    ("u2", "click")
]

separate_event_cnt = {}

for user,event in events:
    if user not in separate_event_cnt:
            separate_event_cnt[user] = {}


    separate_event_cnt[user][event]= separate_event_cnt[user].get(event,0)+1

print(separate_event_cnt)
