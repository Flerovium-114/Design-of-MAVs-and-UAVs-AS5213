import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data
l = np.array([1.11, 2.2, 2.25, 1.95, 1.25, 1.3, 1.12])
w0 = np.array([2.2, 10.7, 7, 8, 1.7, 5.5, 4])

# Define the function
def model(w0, a, c):
    return a * w0**c

# Perform the fitting
popt, pcov = curve_fit(model, w0, l)

a_fit, c_fit = popt

# Generate points for the fitted curve
w0_fit = np.linspace(min(w0), max(w0), 100)
l_fit = model(w0_fit, a_fit, c_fit)

# Plot for fuselage length vs MTOW
plt.figure(figsize=(8, 6))
plt.scatter(w0, l, label='Data')
plt.plot(w0_fit, l_fit, 'r-', label=f'Fit: a={a_fit:.2f}, c={c_fit:.2f}')
plt.xlabel('MTOW (w0)')
plt.ylabel('Fuselage Length (l)')
plt.title("Fuselage Length vs MTOW")
plt.legend()
plt.grid()
plt.show()

# Plot for log-log
plt.figure(figsize=(8, 6))
plt.loglog(w0, l, 'bo', label='Data')
plt.loglog(w0_fit, l_fit, 'r-', label=f'Fit: a={a_fit:.2f}, c={c_fit:.2f}')
plt.xlabel('log(MTOW)')
plt.ylabel('log(Fuselage Length)')
plt.title('Log-Log Plot')
plt.legend()
plt.grid(True, which="both", linestyle='-', color='gray', alpha=0.5)

plt.show()

print(f"The values of a and c are: a = {a_fit:.2f}, c = {c_fit:.2f}")
L_our = a_fit*(5.47**c_fit)
print("L_our: ", L_our)
