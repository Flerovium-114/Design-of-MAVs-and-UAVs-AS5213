import numpy as np
import matplotlib.pyplot as plt

# Input data
l = np.array([1.11, 2.2, 1.95, 2.25])
w = np.array([0.13, 0.27, 0.14, 0.15]) 
h = np.array([0.095, 0.084, 0.22, 0.16])

# Perform linear regression for width
coefficients_w = np.polyfit(l, w, 1)
poly_fit_w = np.poly1d(coefficients_w)

# Perform linear regression for height
coefficients_h = np.polyfit(l, h, 1)
poly_fit_h = np.poly1d(coefficients_h)

# Plotting for width
plt.figure(figsize=(8, 6))
plt.scatter(l, w, label='Width Data')
plt.plot(l, poly_fit_w(l), color='red', label='Linear Regression (Width)')
plt.xlabel('Length')
plt.ylabel('Width')
plt.title('Fuselage width vs length')
plt.legend()
# Annotate the equation of the linear regression line for width
equation_w = f'Width = {coefficients_w[0]:.2f} * Length + {coefficients_w[1]:.2f}'
plt.text(1.2, 0.2, equation_w, fontsize=10, color='black')
plt.grid(True)
plt.show()

# Plotting for height
plt.figure(figsize=(8, 6))
plt.scatter(l, h, label='Height Data')
plt.plot(l, poly_fit_h(l), color='green', label='Linear Regression (Height)')
plt.xlabel('Length')
plt.ylabel('Height')
plt.title('Fuselage height vs length')
plt.legend()
# Annotate the equation of the linear regression line for height
equation_h = f'Height = {coefficients_h[0]:.2f} * Length + {coefficients_h[1]:.2f}'
plt.text(1.3, 0.1, equation_h, fontsize=10, color='black')
plt.grid(True)
plt.show()

# Calculate predicted width and height for l = 1.69
l_value = 1.69
w_predicted = poly_fit_w(l_value)
h_predicted = poly_fit_h(l_value)
print(f'Predicted width for l = {l_value}: {w_predicted}')
print(f'Predicted height for l = {l_value}: {h_predicted}')
