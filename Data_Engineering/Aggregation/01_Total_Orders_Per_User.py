'''
Ask: Sum order amount per user
SQL: select user,sum(order_amount) from orders group by 1;
'''

## Python Method ##
orders = [
    ("u1", 100),
    ("u2", 50),
    ("u1", 75),
    ("u3", 200),
    ("u2", 25)
]

total_order = {}

for user, order in orders:
    total_order[user] = total_order.get(order,0)+order

print(total_order)
