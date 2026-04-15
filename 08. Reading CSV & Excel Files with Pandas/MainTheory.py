# Reading CSV & Excel Files with Pandas
# Why This Matters
# Most real-world data does not start inside your code. It comes from files created by people, systems, or other tools.

# Knowing how to correctly read files is the first step of any data workflow.

# Reading a CSV File
# CSV files are the most common data format.

import pandas as pd
 
df = pd.read_csv("data.csv") # Replace 'data.csv' with the path to your CSV file
print(df)
# Always inspect the data after loading:

df.head()
df.info()

# Never assume the file was read correctly.

# Common CSV Issues
# Custom Separator
pd.read_csv("data.csv", sep=";")

# Skipping Rows
pd.read_csv("data.csv", skiprows=2)

# Selecting Specific Columns
pd.read_csv("data.csv", usecols=["name", "price"])

# Reading Excel Files
# Excel files often contain multiple sheets.

df = pd.read_excel("data.xlsx")

# Read a specific sheet:

pd.read_excel("data.xlsx", sheet_name="Sheet1")

# List all sheet names:

pd.ExcelFile("data.xlsx").sheet_names

# Handling Missing or Broken Data While Reading
pd.read_csv("data.csv", na_values=["NA", "missing", "-"])

# This helps clean data early instead of fixing it later.

# Setting Column Data Types While Reading
pd.read_csv(
    "data.csv",
    dtype={"price": float, "quantity": int}
)

# This prevents data type problems early.

# Reading Large Files Safely
pd.read_csv("data.csv", chunksize=10000)

# This reads the file in smaller pieces instead of loading everything at once.