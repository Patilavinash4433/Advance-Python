
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('A:\\Data Anyletics\\Python\\Advanced Python\\13. Project- Gurgaon Real Estate Market Analysis\\data of gurugram real Estate.csv')
print(df.head())

# print (df.info())

# data cleaning

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.columns)   
df = df.drop_duplicates()
df['price'] = df['price'].astype(str).str.replace('₹', '').str.replace(',', '').astype(float)
df['area'] = df['area'].astype(str).str.replace('sqft', '').str.replace(',', '').astype(float)
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace('₹', '').str.replace(',', '').astype(float)
print(df['price'])
print(df['area'])
print(df['rate_per_sqft'])

# # catgortcial columns cleaning

# df['status'] = df['status'].str.strip().str.lower()
# # df['location'] = df['location'].str.strip().str.lower()
# df['property_type'] = df['property_type'].str.strip().str.lower()

# # Check if 'rera_approved' column exists before processing
# if 'rera_approved' in df.columns:
# 	df['rera_approved'] = df['rera_approved'].str.strip().str.lower()
# 	print(df['rera_approved'])
# else:
# 	print("Column 'rera_approved' not found. Available columns:")
# 	print(df.columns.tolist())
# Business Questions to Answer

# 1. Which is the costliest flat in the dataset?
print("1. Which is the costliest flat in the dataset?\n")
costliest_flat = df.loc[df['price'].idxmax()]
print("Costliest Flat:")
print(costliest_flat)

# 2. Which locality has the highest average price?
print("2. Which locality has the highest average price?\n")
locality_avg_price = df.groupby('locality')['price'].mean().sort_values(ascending=False)
print("Locality with the highest average price:")
print(locality_avg_price.head(1))
    
# 3. Which locality has the highest rate per square foot?
print("3. Which locality has the highest rate per square foot?\n")
locality_avg_rate = df.groupby('locality')['rate_per_sqft'].mean().sort_values(ascending=False)
print("Locality with the highest rate per square foot:")
print(locality_avg_rate.head(1))

# 4. Do ready-to-move properties cost more than under-construction properties?
print("4. Do ready-to-move properties cost more than under-construction properties?\n")
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()
print(f"Average price of ready-to-move properties: {ready_to_move_avg_price}")
print(f"Average price of under-construction properties: {under_construction_avg_price}")

# 5. Do RERA-approved properties command a price premium?
print("5. Do RERA-approved properties command a price premium?\n")
rera_approved_avg_price = df[df['rera_approved'] == 'yes']['price'].mean()
non_rera_approved_avg_price = df[df['rera_approved'] == 'no']['price'].mean()
print(f"Average price of RERA-approved properties: {rera_approved_avg_price}")
print(f"Average price of non-RERA-approved properties: {non_rera_approved_avg_price}")

# 6. How does area (sqft) impact property price?
print("6. How does area (sqft) impact property price?\n")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='area', y='price', data=df)
plt.title('Area vs Price')
plt.xlabel('Area (sqft)')
plt.ylabel('Price (₹)')
plt.show()


# 7. Which BHK configuration is the most expensive on average?
print("7. Which BHK configuration is the most expensive on average?\n")
bhk_avg_price = df.groupby('bhk')['price'].mean().sort_values(ascending=False)
print("BHK configuration with the highest average price:")
print(bhk_avg_price.head(1))
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv') 

# Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df = df.drop_duplicates()

# Numerical Columns Cleaning
df['price'] = df["price"].astype(str).str.replace(",", "").astype(float)
df['area'] = df["area"].astype(str).str.replace(",", "").astype(int)
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(",", "").astype(int)


# Categorical Columns Cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()

df = df.drop_duplicates()

# print(df)
# print(df.info())

# Question 1: Which is the costliest flat in the dataset?
print("1. Which is the costliest flat in the dataset?\n")
costliest_flat = df.loc[df['price'].idxmax()]
print(f"The costliest flat is a {costliest_flat['bhk_count']} BHK flat located in {costliest_flat['locality']} priced at {costliest_flat['price']/10000000} crores in {costliest_flat['society']} society.")

# Question 2: Which locality has the highest average price?
print("2. Which locality has the highest average price?\n")
highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print(f"The locality with the highest average price is {highest_avg_price_locality}.")

# Question 3: Which locality has the highest rate per square foot?
print("3. Which locality has the highest rate per square foot?\n")
highest_rate_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"The locality with the highest rate per square foot is {highest_rate_locality}.")

# Question 4: Do ready-to-move properties cost more than under-construction properties?
print("4. Do ready-to-move properties cost more than under-construction properties?\n")
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()

if ready_to_move_avg_price > under_construction_avg_price:
    print("Ready-to-move properties cost more on average than under-construction properties.")
else:
    print("Under-construction properties cost more on average than ready-to-move properties.")

# Question 5: Do RERA-approved properties command a price premium?
print("5. Do RERA-approved properties command a price premium?\n")
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
rera_not_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()

if rera_approved_avg_price > rera_not_approved_avg_price:
    print("RERA-approved properties command a price premium.")
else:
    print("RERA-approved properties do not command a price premium.")

# Question 6: How does area impact price?
print("6. How does area impact price?\n")
sns.scatterplot(data=df, x='area', y='price')
plt.show()

# Question 7: Which BHK configuration is most expensive based on per sqft rate?
print("7. Which BHK configuration is most expensive based on per sqft rate?\n")
most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive BHK configuration on average is {most_expensive_bhk} BHK.")

# Question 8: Which property type is the costliest?
print("8. Which property type is the costliest?\n")
most_expensive_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive property type is {most_expensive_property_type}.")

# Question 9: Do certain builders price higher?
print("9. Do certain builders price higher?\n")
# print(df.groupby("company_name")["rate_per_sqft"].mean().sort_values(ascending=False).head(5))
# print name of top 5 
print("The top 5 builders that price higher are:", end=" ")
top_5_builders = df.groupby("company_name")["rate_per_sqft"].mean().sort_values(ascending=False).head(5)
for builder in top_5_builders.index:
    print(builder, end=", ")

# Question 10: Are larger homes more expensive per sqft?
print("10. Are larger homes more expensive per sqft?\n")
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.show()
# 8. Which property type (Apartment, Floor, Plot) is the costliest?

print("8. Which property type (Apartment, Floor, Plot) is the costliest?\n")
property_type_avg_price = df.groupby('property_type')['price'].mean().sort_values(ascending=False)
print("Property type with the highest average price:")
print(property_type_avg_price.head(1))


# 9. Do certain builders or companies consistently price higher?
print
print("9. Do certain builders or companies consistently price higher?\n")
builder_avg_price = df.groupby('builder')['price'].mean().sort_values(ascending=False)
print("Builder with the highest average price:")
print(builder_avg_price.head(1))

# 10. Are larger homes always more expensive per square foot?
print
print("10. Are larger homes always more expensive per square foot?\n")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='area', y='rate_per_sqft', data=df)
plt.title('Area vs Rate per Square Foot')
plt.xlabel('Area (sqft)')
plt.ylabel('Rate per Square Foot (₹)')
plt.show()
