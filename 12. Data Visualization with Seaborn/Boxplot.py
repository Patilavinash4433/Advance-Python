import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
tips = sns.load_dataset("tips")

# Create a box plot with a regression line

sns.boxplot(x="day" ,y="tip", data=tips ) # Create a box plot of day vs tip   

plt.show() # Display the plot