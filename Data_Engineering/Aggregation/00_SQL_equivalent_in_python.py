

## Given ##
events = [
    ("u1", "click"),
    ("u2", "view"),
    ("u1", "click"),
    ("u1", "purchase"),
    ("u2", "click"),
    ("u2", "purchase")
]

## SQL Equivalent ##
'''
Count events per user

select user,count(*) from user_events group by 1;

select user,event,count(*) from user_events group by 1,2;

select user,count(distinct event) from user_events group by 1;

select user,event,count(distinct event) from user_events group by 1,2;
'''

## In Python

expected_output_1 = {"u1": 3, "u2": 2}
expected_output_2 = {("u1","click"): 2, ("u2","view"): 2,("u1","purchase"): 1, ("u2","click"): 1}
expected_output_3 = {"click": {"u1","u2"}}
expected_output_4 = {"u1": 2, "u2": 2}

user_cnt = {}


########## expected_output_1 = {"u1": 3, "u2": 2} ###############
for user,event in events:
    user_cnt[user] = user_cnt.get(user,0)+1
    #print(user_cnt)

print(f"User event count: {user_cnt}")

########### expected_output_2 = {("u1","click"): 2, ("u2","view"): 2,("u1","purchase"): 1, ("u2","click"): 1} #########
user_event_cnt = {}
for user,event in events:
    user_event_cnt[user,event] = user_event_cnt.get((user,event),0)+1
print(f"Count by user events: {user_event_cnt}")

########## expected_output_3 = {"click": {"u1","u2"}} #################

user_event = {}

for user,event in events:
    if event not in user_event:
        user_event[event] = set()

    user_event[event].add(user)
print(f"unique events: {user_event}")

########## expected_output_3 = {1: {"u1","u2"},2: {"u2","u3"} } #################

user_event_cnt_1 = {}
user_event_cnt_2 = {}
for user,event in events:
    if user not in user_event_cnt_1:
        user_event_cnt_1[user]= set()
    user_event_cnt_1[user].add(event)

print(user_event_cnt_1)

for user,event in user_event_cnt_1.items():
    if len(event) not in user_event_cnt_2:
        user_event_cnt_2[len(event)] = set()
    user_event_cnt_2[len(event)].add(user)

print(user_event_cnt_2)





