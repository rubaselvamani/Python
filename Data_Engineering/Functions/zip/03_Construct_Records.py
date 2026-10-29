users = ["u1", "u2", "u3"]
events = ["click", "view", "purchase"]

records = []

for user, event in zip(users, events):
    records.append({
        "user": user,
        "event": event
    })

print(records)
