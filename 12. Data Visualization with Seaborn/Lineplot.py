import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
tips = sns.load_dataset("tips")

# Create a line plot with a regression line

sns.lineplot(x="size", y="tip", data=tips , hue="sex") # Create a scatter plot of total bill vs tip   

plt.show() # Display the plot
