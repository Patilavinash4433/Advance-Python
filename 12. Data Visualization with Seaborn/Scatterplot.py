import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
tips = sns.load_dataset("tips")

# Create a scatter plot with a regression line

sns.scatterplot(x="total_bill", y="tip", data=tips , hue="sex") # Create a scatter plot of total bill vs tip
sns.set_theme(style="whitegrid") # Set the theme for the plot
sns.regplot(x="total_bill", y="tip", data=tips, scatter=False, color="red") # Add a regression line to the scatter plot
plt.show() # Display the plot
