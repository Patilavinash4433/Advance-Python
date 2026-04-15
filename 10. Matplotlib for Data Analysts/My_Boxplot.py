import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # Generate 1000 random data points from a normal distribution
plt.boxplot(data , patch_artist=True, boxprops=dict(facecolor='lightblue'))  # Create a boxplot of the data
plt.title('Boxplot of Random Data')  # Set the title of the plot
plt.ylabel('Values')  # Set the label for the y-axis
plt.show()  # Display the plot