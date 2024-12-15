import matplotlib.pyplot as plt
import numpy as np
import math

cd0 = 0.0231
K = 0.04876
v = np.linspace(1, 50, 1000)
cl = []
w = 5.47 * 9.81
rho = 1.2
S = 0.42
P = []

for i in range(len(v)):
    cl_temp = 2*w/(rho*(v[i]**2)*S)
    P_temp = (cd0 + K*(cl_temp**2))*v[i]*(0.5*rho*S*(v[i]**2))
    cl.append(cl_temp)
    P.append(P_temp)

plt.plot(v, P, color = 'black', label = '$P_{req}$')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Power (W)')
plt.title('Power vs Velocity')
plt.grid(True)

# Draw a horizontal line at the minimum point
min_P = min(P)
min_index = P.index(min_P)
plt.axhline(y=min_P, xmin=0, xmax=v[min_index]/max(v), color='r', linestyle='--', label='$P_{\min}$', alpha=0.6)

# Draw a vertical line at the corresponding velocity
min_velocity = v[min_index]
plt.axvline(x=min_velocity, ymin = 0, ymax=min_P / max(P) , color='g', linestyle='--', label=f'$V_{{P_{{\min}}}}$ ({min_velocity:.2f} m/s)', alpha=0.6)

plt.legend(loc='best', fontsize='small')
plt.show()