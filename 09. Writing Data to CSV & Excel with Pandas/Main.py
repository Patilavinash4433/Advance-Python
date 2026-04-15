import pandas as pd

# Creaate a DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
}   

df = pd.DataFrame(data)

data2 = {
    "name": ["David", "Eve", "Frank"],
    "age": [28, 32, 40],
    "city": ["Houston", "Phoenix", "Seattle"]
}
df2 = pd.DataFrame(data2)
print(df)

# Write to CSV
df.to_excel("output.xlsx", index=False)  # Replace 'output.xlsx' with your desired file path

with pd.ExcelWriter("output2.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Sheet1", index=False)
    df2.to_excel(writer, sheet_name="Sheet2", index=False)
