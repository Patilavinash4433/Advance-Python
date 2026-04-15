# Saving Plots
# We can save our plots to image files like PNG for sharing or reports.
import matplotlib.pyplot as plt
import numpy as np

plt.savefig("Main.png", bbox_inches="tight")

# We can also save in other formats like JPG, SVG, PDF, etc. For instance:

plt.savefig("Main.pdf")

# Save before plt.show().

# Real Data Analytics Example
days = np.arange(1, 8)
sales = [120, 150, 170, 160, 180, 200, 220]
 
plt.figure(figsize=(6,4))
plt.plot(days, sales, marker="o")
plt.title("Weekly Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# What this tells:

# Trend direction
# Growth pattern
# Business insight in one glance

