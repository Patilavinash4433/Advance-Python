# Pandas Basics & Why Pandas
# The Problem Pandas Solves
# Real-world data is usually:

# tabular
# messy
# stored in files
# full of missing or inconsistent values
# Working with such data using only lists and dictionaries quickly becomes hard to manage.

# Pandas exists to make working with tabular data simple and structured.

# What Pandas Really Is
# Pandas provides a data structure called a DataFrame.

# A DataFrame:

# looks like a table
# has rows and columns
# keeps data aligned by column name
# lets you work with the whole column at once
# Think of it as a spreadsheet that you control with code.

# Creating a DataFrame
# From a dictionary:

import pandas as pd
 
data = {
    "name": ["Ali", "Sara", "John"],
    "marks": [85, 90, 78]
}
 
df = pd.DataFrame(data)

# Each key becomes a column.

# Looking at the Data
# Before doing anything, you inspect the data.

df.head()
df.info()
df.describe()

# What columns exist
# What data types are present
# Are there missing values
# How big the dataset is
# Selecting Data
# Select a column:

df["marks"]
print(df["name"])
print(df["marks"]) 
print(df[["name", "marks"]])
print(df["marks"].mean())
print(df["marks"].max())
print(df["marks"].min())
print(df["marks"].std())
print(df["marks"].var())

# Select multiple columns:

# df[["name", "marks"]]

# This column-based thinking is central to Pandas.

# Rows and Index
# Each row has an index. By default, it is just a number.

# The index helps Pandas:

# align data
# keep rows connected across operations
# You usually do not need to change it early on.

# Why Pandas Is Used for Data Work
# Pandas makes it easy to:

# load data from files
# clean and transform data
# analyze columns instead of individual values
# keep data readable and organized
# This is why Pandas is the foundation of most data analysis workflows.
import pandas as pd

df = pd.DataFrame({
    "Product Name": [" iPhone 14 ", "Samsung Galaxy", " OnePlus 11", "Pixel 7 ", None] * 200,
    "price": ["499", "799", "1199", "899", None] * 200,
    "category": ["Mobile", " mobile ", "ELECTRONICS", "Electronics ", None] * 200,
    "rating": [5, 4, None, 3, 2] * 200,
    "reviews": [1200, 3400, 560, 780, 150] * 200,
    "in_stock": ["Yes", "No", "yes ", " no", None] * 200,
    "launch_year": ["2023", "2022", "2021", "2020", None] * 200
})