import matplotlib.pyplot as plt
import numpy as np
import math

v = np.linspace(1, 30, 100)
T_w = 1/17.826
w = 5.47 * 9.81
rho = 1.2
S = 0.42
cl_max = 1.43
cl_min = 1.24
v_stall = math.sqrt(2*w/(rho*S*cl_max))
v_stall_min = math.sqrt(2*w/(rho*S*cl_min))
w_s = w/S
K = 1/(math.pi*0.816*8)
cd0 = 0.0231

print(v_stall)

n = []
n1 = []

for i in range(len(v)):
    n_temp = 0.5*1.2*v[i]**2*cl_max/w_s
    n_temp = min(n_temp, 2.5)
    n.append(n_temp)
    n_min_temp = -0.5*1.2*v[i]**2*cl_min/w_s
    n_min_temp = max(n_min_temp,-1)
    n1.append(n_min_temp)

plt.plot(v,n, label = 'positive stall curve')
plt.plot(v,n1, label = 'negative stall curve')
plt.plot([v[0], v[0]], [n[0], n1[0]], color='black', alpha=0.5)
plt.plot([v[-1], v[-1]], [n[-1], n1[-1]], color='green', alpha=0.5, label = 'red-line speed')
plt.title("V-n Diagram")
plt.xlabel("V")
plt.ylabel("n")
plt.ylim(-3, 4)
plt.legend(loc = 'upper left')
plt.grid()
plt.show()