import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import linearregression
model = LinearRegression()

# # Train the model (fitting the line to the data)
model.fit(linearregression.area.reshape(-1, 1), linearregression.price)  # Reshape area for compatibility

# Get the slope (coefficient) and intercept of the regression line
m = model.coef_[0]  # Slope
b = model.intercept_  # Intercept

print("Slope (m):", m)
print("Intercept (b):", b)
# Predict price for a house with 8000 square feet
predicted_price = m * 8000 + b
print("Predicted Price for 8000 sq ft:", predicted_price)

