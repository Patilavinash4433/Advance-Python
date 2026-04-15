import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
tips = sns.load_dataset("tips")

# Create a count plot with a regression line

sns.countplot(x="day" ,data=tips ) # Create a count plot of size vs sex   

plt.show() # Display the plot
