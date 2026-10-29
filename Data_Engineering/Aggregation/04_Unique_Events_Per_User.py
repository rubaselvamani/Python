'''
Step 1: Select distinct user,event from user_event_tble
Step 2: Convert rows into columns if all events need to be kept in a single row
'''

## In Python ##
events = [
    ("u1", "click"),
    ("u1", "view"),
    ("u1", "click"),
    ("u2", "view"),
    ("u2", "purchase")
]

unique_events = {}

for user,event in events:
    if user not in unique_events:
        unique_events[user] = set()

    unique_events[user].add(event)

print(unique_events)
