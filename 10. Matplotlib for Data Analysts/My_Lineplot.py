import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 20]

plt.title("Sample Line Plot")
plt.plot(x,y , marker='o', linewidth=2, linestyle='--', color='b', label='Data Points')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()



