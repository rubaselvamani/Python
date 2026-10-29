'''
Sliding Window (Max 7 day sale (SUM) and when did it start)
SQL: Max windows funtion with preceding and proceding logic as needed
'''


sales = [10, 20, 30, 40, 50, 60, 70, 80, 90]
k =7

current_sale = sum(sales[:k])
best_sale = current_sale
start_date = None

if k<= 0 or k > len(sales):
 best_sale = 0

for right in range(k,len(sales)):
    current_sale += sales[right]
    current_sale -= sales[right-k]

    if current_sale > best_sale:
        best_sale = current_sale
        start_date = right-k+1

print(best_sale,start_date)
