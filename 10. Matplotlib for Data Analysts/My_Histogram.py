import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # Generate 1000 random data points from a normal distribution
plt.hist(data, bins=30, color='m', alpha=0.7 , edgecolor='black')  # bins is the number of bars in the histogram
plt.title("Sample Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

