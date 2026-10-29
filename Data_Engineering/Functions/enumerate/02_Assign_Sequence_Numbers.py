events = [
    ("u1", "click"),
    ("u2", "view"),
    ("u1", "purchase")
]

for sequence, event in enumerate(events, start=1):
    print(sequence, event)
