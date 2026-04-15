# Data Visualization with Seaborn
# Seaborn is a powerful Python library for data visualization built on top of Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

# 1. The Real Question
# Why do we even need Seaborn?
# We already have Matplotlib. So why another library?

# Because Matplotlib is hard for analysis.

# In real data analytics, our goal is not to draw charts. Our goal is to understand data quickly.

# Seaborn exists to answer questions like:

# Is there a relationship between two columns?
# How does a number behave across categories?
# Are there outliers?
# Which features are correlated?
# Seaborn helps you see patterns in one line of code.

# 2. Think Like an Analyst
# Task	Matplotlib	Seaborn
# Draw a chart	Good	Good
# Explore data quickly	Hard	Very easy
# Default visuals	Basic	Excellent
# Statistical meaning	Manual	Built-in
# Pandas friendly	Okay	Excellent
# Rule of thumb

# Seaborn for understanding
# Matplotlib for fine control
# 3. Installation and Import
# pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt

# 4. Seaborn Works on DataFrames (This Is Key)
# Seaborn is designed for tabular data.

df = sns.load_dataset("tips")
df.head()

# Instead of passing lists and arrays, you pass:

# column names
# the full DataFrame
# This makes analysis much faster.

# 5. The Most Important Idea in Seaborn
# Almost every Seaborn plot looks like this:

sns.plot_name(x="column1", y="column2", data=df)

# You describe:

# what is on x
# what is on y
# where the data lives
# That is it.

# 6. The 6 Seaborn Plots You Actually Need
# You do not need to learn everything.

# These 6 plots cover almost all analytics use cases.

# 6.1 Scatter Plot
# Relationship between two numbers
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.show()

# Why we use it:

# Is there correlation?
# Do values increase together?
# Are there clusters?
# Add category comparison:

sns.scatterplot(
    x="total_bill",
    y="tip",
    hue="sex",
    data=df
)

# 6.2 Line Plot
# Trend with automatic averaging
sns.lineplot(x="size", y="tip", data=df)
plt.show()

# Why Seaborn is special here:

# It automatically calculates the mean
# Shows trends, not raw noise
# 6.3 Count Plot
# How many times something occurs
sns.countplot(x="day", data=df)
plt.show()

# Why we use it:

# Distribution of categories
# Class imbalance
# Most common values
# With split:

sns.countplot(x="day", hue="sex", data=df)

# 6.4 Bar Plot
# Average value per category
sns.barplot(x="day", y="total_bill", data=df)
plt.show()

# Important:

# This shows mean, not sum
# Confidence interval is shown by default
# This is why Seaborn is powerful for analysis.

# 6.5 Box Plot
# Spread, median, and outliers
sns.boxplot(x="day", y="total_bill", data=df)
plt.show()

# Why analysts love it:

# See outliers instantly
# Compare distributions across groups
# 6.6 Heatmap
# Relationships between numeric columns
corr = df.corr(numeric_only=True)
 
sns.heatmap(corr, annot=True)
plt.show()

# Why this is critical:

# Feature selection
# Understanding dependencies
# Detecting redundancy
# 7. One Example That Explains Everything
sns.boxplot(
    x="day",
    y="tip",
    hue="sex",
    data=df
)
plt.show()

# In one plot you see:

# Day-wise comparison
# Gender-wise comparison
# Spread and outliers
# Doing this in Matplotlib would take much more code.

# 8. Styling Is Secondary (But Easy)
sns.set_theme(style="whitegrid")

# This is not the main reason we use Seaborn. Insight comes first. Looks come later.

# 9. When Should You Use Seaborn First?
# Use Seaborn when:

# You open a new dataset
# You are doing EDA
# You want quick insights
# You want statistically meaningful plots
# Use Matplotlib when:

# You need full control
# You are exporting final visuals
# You are building dashboards
# Final Summary (Say This Clearly in the Video)
# We use Seaborn because:

# It understands data, not just pixels
# It works directly with DataFrames
# It shows statistics automatically
# It helps us think like analysts
# Seaborn is not about pretty charts. It is about understanding data fast.