# Selecting, Filtering & Data Cleaning with Pandas
# Raw data is rarely ready for analysis. Before asking questions, you must select the right data, filter what you need, and clean what is broken.
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
# This step decides whether your results are trustworthy.

# Selecting Columns
# Select a single column:

df["price"]

# Select multiple columns:

df[["price", "category", "rating"]]

# Column selection is the most common operation in Pandas.

# Selecting Rows with Conditions
# Filter rows using conditions:

df[df["price"] > 500]

# Multiple conditions:

df[(df["price"] > 500) & (df["rating"] >= 4)]

# This is how questions become answers.

# Handling Missing Values
# Check missing data:

df.isna()
df.isna().sum()

# Remove missing values:

# df.dropna()

# Fill missing values:

df["rating"] = df["rating"].fillna(df["rating"].mean())

# Always decide whether to remove or fill based on context.

# Renaming Columns
# Clean column names early:

df = df.rename(columns={"Product Name": "product_name"})

# Clean column names make code readable and consistent.

# Changing Data Types
# Check data types:

df.dtypes

# Convert types:

df["price"] = df["price"].astype(float)

# Incorrect data types lead to incorrect analysis.

# Removing Duplicates
df.drop_duplicates()

# Duplicates silently distort results if not handled.

# Basic String Cleaning
df["category"] = df["category"].str.lower().str.strip()

# String cleaning is common in real-world datasets.

# Commonly Used Pandas Functions
# Purpose	Function
# View first rows	     |  head()
# Dataset summary	     |  info()
# Statistical summary	 |  describe()
# Select column	         |  df["col"]
# Filter rows	         |  df[condition]
# Check missing values	 |  isna()
# Remove missing values	 |  dropna()
# Fill missing values	 |  fillna()
# Rename columns	     |  rename()
# Change data type	     |  astype()
# Remove duplicates	     |  drop_duplicates()
# String operations	     |  str.lower(), str.strip()

