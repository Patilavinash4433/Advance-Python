import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 20]

plt.scatter(x, y, s=100, marker='o', color='r', label='Data Points', alpha=0.7)  # s is the size of the points
plt.title("Sample Scatter Plot")    
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
