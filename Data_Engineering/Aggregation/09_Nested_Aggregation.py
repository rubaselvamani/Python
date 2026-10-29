
'''
Nested aggregation

'''

#Calculate total sales by country and product.

sales = [
    ("US", "phone", 100),
    ("US", "phone", 200),
    ("US", "laptop", 500),
    ("IN", "phone", 150),
    ("IN", "laptop", 400)
]
total_sales = {}

for country,product,sale in sales:
    if country not in total_sales:
        total_sales[country] = {}
    total_sales[country][product] = total_sales[country].get(product,0)+sale

print(total_sales)

#output: {'US': {'phone': 300, 'laptop': 500}, 'IN': {'phone': 150, 'laptop': 400}}
