
import pandas as pd

# Reading a CSV file

# df = pd.read_csv("A:\\Data Anyletics\\Python\\Advanced Python\\08. Reading CSV & Excel Files with Pandas\\data.csv",skiprows=2 , usecols=["order_id", "city"])  # Replace 'data.csv' with the path to your CSV file
# print(df)
# print(df.head())  # Display the first 5 rows of the DataFrame
# print(df.info())  # Get information about the DataFrame
# print(df.describe())  # Get statistical summary of the DataFrame
#select all Deleveried
# df_delivered = df[df['order_status'] == 'Delivered']
# print(df_delivered)
# pd.read_csv("data.csv", sep=";")
# pd.read_csv("data.csv", skiprows=2)

# df2 = pd.read_excel("A:\\Data Anyletics\\Python\\Advanced Python\\08. Reading CSV & Excel Files with Pandas\\Random Data Generator.xlsx")  # Replace 'data.xlsx' with the path to your Excel file
# print(df2)

df2 = pd.read_excel(
    "A:\\Data Anyletics\\Python\\Advanced Python\\08. Reading CSV & Excel Files with Pandas\\Random Data Generator.xlsx", sheet_name="Sheet2",
    dtype={"order_id": int}
)
print(df2)
