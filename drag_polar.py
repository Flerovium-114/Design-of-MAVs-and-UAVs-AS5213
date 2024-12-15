import matplotlib.pyplot as plt
import numpy as np
import math

K = 1/(math.pi*0.816*8)
cl = np.linspace(0, 2, 100)
cd = 0.0231 + K * cl**2

plt.plot(cd, cl, label=r'$C_D = 0.0231 + KC_L^2$')
plt.title("Drag Polar")
plt.ylabel('Lift Coefficient ($C_L$)')
plt.xlabel('Drag Coefficient ($C_D$)')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(cl, cd, label=r'$C_D = 0.0231 + KC_L^2$')
plt.title("Drag Polar")
plt.xlabel('Lift Coefficient ($C_L$)')
plt.ylabel('Drag Coefficient ($C_D$)')
plt.legend()
plt.grid(True)
plt.show() 



