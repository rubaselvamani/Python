
events = [
    ("u1", "click"),
    ("u2", "view"),
    ("u1", "purchase")
]

result = []

for sequence, event in enumerate(events, start=1):
    user, event_type = event

    result.append({
        "sequence": sequence,
        "user": user,
        "event": event_type
    })
    
print(result)
