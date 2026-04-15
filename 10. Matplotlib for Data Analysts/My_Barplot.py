import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 15, 7, 12, 20]

plt.bar(x, y, color='c' )  # alpha is for transparency
plt.title("Sample Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values") 
plt.legend()  # Add legend to the plot ye kaam karta hai ki agar aapne plot me label diya hai to wo legend me show hoga legend me aapko ye bhi specify karna hota hai ki aapko legend me kya dikhana hai, iske liye aap label parameter ka use kar sakte hain jab aap plot bana rahe hote hain. Jaise ki maine yaha par label='Data Points' diya hai to wo legend me show hoga.
plt.show()

