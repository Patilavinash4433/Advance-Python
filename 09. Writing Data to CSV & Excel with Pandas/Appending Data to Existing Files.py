import pandas as pd 

# Create a DataFrame of ecommerce orders
df = pd.DataFrame({
    'order_id': [1001, 1002, 1003, 1004],
    'customer_id': [501, 502, 503, 504],
    'order_amount': [250.75, 89.99, 150.00, 300.50],
    'order_date': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18'],
    'customer_name': ['Alice', 'Bob', 'Charlie', 'David'],
    'customer_country': ['USA', 'Canada', 'USA', 'UK']
})

df.to_csv('ecommerce_orders.csv', mode="a", header=False, index=False)