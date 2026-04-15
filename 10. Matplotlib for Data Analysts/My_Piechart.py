import matplotlib.pyplot as plt
import numpy as np


Sizes = [40 , 30 , 20 , 10]  # Define the sizes of each slice of the pie chart
lables = ['xl ' , 'l' , 'm' , 's']  # Define the labels for each slice of the pie chart
plt.pie(Sizes , labels=lables , autopct='%1.1f%%' , startangle=90)  # Create a pie chart with the specified sizes and labels
plt.title('Sizes Distribution')  # Set the title of the plot
plt.axis('equal')  # Ensure that the pie chart is circular
plt.show()  # Display the plot
