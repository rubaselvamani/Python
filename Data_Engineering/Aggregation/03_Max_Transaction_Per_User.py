
'''
SQl : Select user, max(transactions) from transactions_tbl;
'''

## In Python ##

transactions = [
    ("u1", -100),
    ("u1", -250),
    ("u1", -75),
    ("u2", 50),
    ("u2", 300)
]

max_transaction = {}

for user,tran in transactions:
    if user not in max_transaction:
# This step is important, otherwise max transaction would be defaulted zero due to negative transaction value. No need to start with max_transaction[user] as 0
        max_transaction[user] = tran 
    max_transaction[user] = max(max_transaction[user],tran)


print(max_transaction)
