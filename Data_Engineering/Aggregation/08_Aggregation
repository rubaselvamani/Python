
orders = [
    {"user": "u1", "amount": 100},
    {"user": "u2", "amount": 50},
    {"user": "u1", "amount": 75},
    {"user": "u2", "amount": 25}
]



result = {}
for order in orders:

    user = order["user"]
    amount = order["amount"]

    result[user] = result.get(user, 0) + amount

print(result)

#output: {'u1': 175, 'u2': 75}

