import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# Sample data (area in square feet, price in thousands of dollars)
area = np.array([2000, 3000, 5000, 7000, 10000, 12000])
price = np.array([250, 350, 500, 650, 800, 1000])
plt.scatter(area, price)
plt.xlabel("Area (Square Feet)")
plt.ylabel("Price (Thousands of Dollars)")
plt.title("House Area vs. Price")
plt.grid(True)
plt.show()
# Create the model
