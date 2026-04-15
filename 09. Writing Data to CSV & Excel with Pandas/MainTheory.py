# Writing Data to CSV & Excel with Pandas
# Why This Matters
# Data analysis is incomplete until results are saved or shared. Often, your final output is not a plot or a model, but a clean file that others can use.

# Pandas makes exporting data simple and reliable.
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
# Writing to a CSV File
# Save a DataFrame as a CSV file:

df.to_csv("clean_data.csv", index=False)

# index=False is commonly used to avoid writing row numbrs.

# Writing to an Excel File
# Save a DataFrame to Excel:

df.to_excel("clean_data.xlsx", index=False)

# This creates a single-sheet Excel file.

# Writing Multiple Sheets to Excel
with pd.ExcelWriter("report.xlsx") as writer:
    #df_sales.to_excel(writer, sheet_name="Sales", index=False)
    #df_users.to_excel(writer, sheet_name="Users", index=False)
    pass

# This is useful for reports and dashboards.

# Appending Data to Existing Files
# Append to a CSV file:

df.to_csv("log.csv", mode="a", header=False, index=False)

# Use this carefully to avoid duplicate data.

# Controlling Output Format
# Change separator:

df.to_csv("data.csv", sep=";")

# Control missing values:

df.to_csv("data.csv", na_rep="NA")

# Saving Only What You Need
# Always export:

# only required columns
# cleaned and validated data
# Example:

df[["name", "price", "rating"]].to_csv("final_output.csv", index=False)
# This ensures your output is concise and relevant.

