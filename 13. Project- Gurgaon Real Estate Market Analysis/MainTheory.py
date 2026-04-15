# Project: Gurgaon Real Estate Market Analysis
# 1. Problem Statement
# Background
# You are working as a Data Analyst for a real estate advisory firm operating in Gurgaon. The firm spent significant time to collect data on residential properties across various localities in Gurgaon. The firm wants data-backed insights to guide buyers, investors, and developers in making informed real estate decisions.

# You are provided with a dataset containing residential property listings across multiple sectors of Gurgaon.
# The dataset includes pricing, area, BHK configuration, property type, builder details, and RERA approval status.

# Dataset link: https://www.kaggle.com/datasets/nikhilmehrahr26/gurgaon-real-estate-dataset?resource=download

# If the dataset link is broken, we have also added the dataset for your download below.

# Business Questions to Answer
# Your analysis should answer the following business questions clearly.

# Which is the costliest flat in the dataset?
# Which locality has the highest average price?
# Which locality has the highest rate per square foot?
# Do ready-to-move properties cost more than under-construction properties?
# Do RERA-approved properties command a price premium?
# How does area (sqft) impact property price?
# Which BHK configuration is the most expensive on average?
# Which property type (Apartment, Floor, Plot) is the costliest?
# Do certain builders or companies consistently price higher?
# Are larger homes always more expensive per square foot?
# 2. Solution Overview
# We will solve this problem using Exploratory Data Analysis (EDA).
# EDA helps us understand patterns, relationships, and anomalies in the data before applying any advanced modeling.

# The solution is divided into logical steps:

# Data loading and understanding
# Data cleaning and preparation
# Analysis to answer each business question
# Summary of insights
# Each step below explains what we are doing and why.

# 3. Data Loading and Initial Understanding
# Step 1: Import Required Libraries
# We use Pandas for data manipulation and Matplotlib and Seaborn for visualization.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the Dataset
from turtle import pd


df = pd.read_csv("gurgaon_real_estate.csv")
df.head()

# Why this step matters:

# Allows us to inspect the structure of the dataset
# Helps verify column names and data types
# Step 3: Basic Dataset Overview
df.shape
df.info()

# Why this step matters:

# Identifies number of rows and columns
# Reveals missing values and incorrect data types
# 4. Data Cleaning and Preparation
# Real-world datasets are messy. Cleaning ensures accurate analysis.

# Step 4: Standardize Column Names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Why:

# Makes column names consistent and easier to use in code
# Step 5: Convert Numeric Columns
df["price"] = df["price"].astype(str).str.replace(",", "").astype(int)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)

# Why:

# Numeric calculations are impossible if values are stored as strings
# Step 6: Clean Categorical Columns
df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower()
df["flat_type"] = df["flat_type"].str.strip().str.lower()

# Why:

# Avoids duplicate categories caused by inconsistent formatting
# Step 7: Remove Duplicates
df = df.drop_duplicates()

# Why:

# Duplicate rows can skew averages and insights
# 5. Answering Business Questions with Analysis
# Question 1: Which is the costliest flat?
df.loc[df["price"].idxmax()]

# Why:

# Identifies the highest priced property directly
# Question 2: Which locality has the highest average price?
df.groupby("locality")["price"].mean().sort_values(ascending=False)

# Why:

# Grouping helps compare average prices across localities
# Question 3: Which locality has the highest rate per square foot?
df.groupby("locality")["rate_per_sqft"].mean().sort_values(ascending=False)

# Why:

# Rate per sqft highlights premium locations independent of property size
# Question 4: Ready-to-move vs Under-construction pricing
df.groupby("status")["price"].median()

# Why:

# Median is preferred over mean due to outliers in property prices
# Question 5: Does RERA approval affect pricing?
df.groupby("rera_approval")["price"].median()

# Why:

# Helps measure trust premium associated with regulatory approval
# 6. Deeper Insights
# Question 6: How does area impact price?
sns.scatterplot(x="area", y="price", data=df)
plt.show()

# Why:

# Visual inspection reveals correlation and pricing behavior
# Question 7: Which BHK configuration is most expensive?
df.groupby("bhk_count")["price"].mean()

# Why:

# Helps identify demand and pricing by family size
# Question 8: Which property type is the costliest?
df.groupby("flat_type")["price"].mean()

# Why:

# Compares Apartments, Floors, and Plots fairly
# Question 9: Do certain builders price higher?
df.groupby("company_name")["price"].mean().sort_values(ascending=False)

# Why:

# Captures brand and trust impact on pricing
# Question 10: Are larger homes more expensive per sqft?
sns.scatterplot(x="area", y="rate_per_sqft", data=df)
plt.show()

# Why:

# Helps evaluate economies of scale in real estate pricing
# 7. Final Insights Summary
# From the analysis, we can conclude:

# Premium localities consistently show higher prices and rate per sqft
# Ready-to-move and RERA-approved properties tend to command higher prices
# Builder reputation significantly impacts property pricing
# Larger homes are not always more expensive per sqft
# Apartments generally have higher rate per sqft than plots and floors