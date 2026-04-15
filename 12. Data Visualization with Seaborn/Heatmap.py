import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
df = sns.load_dataset("tips")
print(df.head()) # Display the first few rows of the dataset
# Create a heatmap of the correlation matrix
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show() # Display the plot

