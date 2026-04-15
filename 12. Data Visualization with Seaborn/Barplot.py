import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
tips = sns.load_dataset("tips")

# Create a bar plot with a regression line

sns.barplot(x="day", y = "tip" ,data=tips ) # Create a count plot of size vs sex   

plt.show() # Display the plot