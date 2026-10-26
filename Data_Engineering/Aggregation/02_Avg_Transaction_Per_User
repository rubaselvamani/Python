'''
AsK Average transaction amount per user

SQL Calculation: Avg transaction = total amount/ total_transactions
'''

#### Python Method ##

transactions = [
    ("u1", 100),
    ("u1", 50),
    ("u2", 40),
    ("u2", 60),
    ("u2", 20)
]
total_orders = {}

total_amt = 0
total_tran = 0
for user,amount in transactions:
   if user not in total_orders:
       total_orders[user] = { "total amount":0, "total tran" : 0}

   total_orders[user]["total amount"] += amount
   total_orders[user]["total tran"] += 1

print(total_orders)

avg_amount = {}
for user,entry in total_orders.items():
    avg_amount[user] = entry["total amount"] / entry["total tran"]
print(avg_amount)
