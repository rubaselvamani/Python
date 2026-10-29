'''
Count unique products purchased per user
SQL: Select user, count(distinct event) from user_event_tbl group by 1
'''

## In Python ##
purchases = [
    ("u1", "p1"),
    ("u1", "p2"),
    ("u1", "p1"),
    ("u2", "p3"),
    ("u2", "p4")
]

unique_purchase = {}

for user,product in purchases:
    if user not in unique_purchase:
        unique_purchase[user] = set()

    unique_purchase[user].add(product)

print(unique_purchase)

unique_purchase_cnt = {}

for user, unique_product in unique_purchase.items():
    print(user, unique_product)
    print(unique_purchase.items())
    unique_purchase_cnt[user] = len(unique_product)

print(unique_purchase_cnt)
