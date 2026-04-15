import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 8)
sales = [120, 150, 170, 160, 180, 200, 220]

plt.figure(figsize=(6,4))
plt.plot(days, sales, marker="o")
plt.title("Weekly Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
