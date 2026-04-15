# Matplotlib for Data Analysts
# 1. What is Matplotlib and Why It Exists
# Matplotlib is a low-level plotting library in Python that gives you full control over visualizations.

# Why Matplotlib matters:

# Foundation of almost every Python plotting library
# Works with NumPy arrays directly
# Maximum control over plots (labels, ticks, layout, styles)
# Industry standard for custom, publication-ready plots
# Seaborn, pandas .plot(), etc. are all built on top of Matplotlib.

# 2. Installation and Import
# pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np

# 3. Basic Plot Anatomy
# Every Matplotlib plot has:

# Figure → entire canvas
# Axes → actual plotting area
# Data → lines, bars, points
# Basic example:

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
 
plt.plot(x, y)
plt.show()

# 4. Most Important Plot Types (Must-Know)
# 4.1 Line Plot
# Used for trends over time or continuous data.

plt.plot(x, y)
plt.title("Line Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Useful parameters:

plt.plot(x, y, color="red", linewidth=2, linestyle="--", marker="o")

# 4.2 Scatter Plot
# Used to show relationship between two variables.

plt.scatter(x, y)
plt.show()

# Common options:

plt.scatter(x, y, s=100, c="green", alpha=0.7)

# 4.3 Bar Chart
# Used for categorical comparisons.

categories = ["A", "B", "C"]
values = [20, 35, 30]
 
plt.bar(categories, values)
plt.show()

# Horizontal bar:

plt.barh(categories, values)

# 4.4 Histogram
# Used to show distribution of data.

data = np.random.randn(1000)
 
plt.hist(data, bins=30)
plt.show()

# Key parameters:

plt.hist(data, bins=30, edgecolor="black")

# 4.5 Box Plot
# Used to detect outliers and spread.

plt.boxplot(data)
plt.show()

# 4.6 Pie Chart (Use Carefully)
# Only for very small categories.

sizes = [40, 35, 25]
labels = ["A", "B", "C"]
 
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.show()

# 5. Titles, Labels, Legends (Very Important)
plt.plot(x, y, label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.legend()
plt.show()

# 6. Multiple Lines on One Plot
y2 = [12, 18, 22, 28]
 
plt.plot(x, y, label="Product A")
plt.plot(x, y2, label="Product B")
plt.legend()
plt.show()

# 7. Figure Size and DPI (Presentation Ready)
plt.figure(figsize=(8, 4), dpi=100)
plt.plot(x, y)
plt.show()

# 8. Subplots (Multiple Charts Together)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
 
axes[0].plot(x, y)
axes[0].set_title("Line Plot")
 
axes[1].bar(categories, values)
axes[1].set_title("Bar Chart")
 
plt.show()

# 9. Grid, Ticks, and Limits
# Grid
plt.grid(True)

# Axis Limits
plt.xlim(0, 5)
plt.ylim(0, 30)

# Custom Ticks
plt.xticks([1, 2, 3, 4])
plt.yticks([10, 20, 30])

# 10. Styles (One Line Magic)
plt.style.use("ggplot")

# Other common styles:

# seaborn-v0_8
# dark_background
# classic
# 11. Saving Plots (Very Important for Analytics)
# plt.savefig("plot.png", bbox_inches="tight")

# Save before plt.show().

# 12. Real Data Analytics Example
days = np.arange(1, 8)
sales = [120, 150, 170, 160, 180, 200, 220]
 
plt.figure(figsize=(6,4))
plt.plot(days, sales, marker="o")
plt.title("Weekly Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# What this tells:

# Trend direction
# Growth pattern
# Business insight in one glance