# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
clalphaw = 0.0812

# %%
Clto = 1.4
Cdto = 0.04 + 0.048*Clto**2
Swing = 0.42
Lwf = 0.5*1.225*(15.38/1.1)**2*Clto*Swing
print(Lwf)
D = 0.5*1.225*(15.38/1.1)**2*Cdto*Swing
Cmacw = -0.05
Cwing = 0.23
Macwing = 0.5*1.225 * (15.38/1.1)**2 * Cmacw * Cwing

# %%
CMalpha = -2.069
I = 1.075
topas = 0
bel = 0.85
maxdefp = 20
maxdefn = -25
tvrh = 0.685
tef = 0.9
clalphah= 0.071
btail = 0.606
taue = 0.4
Stail = 0.069
Swing= 0.42
Weight= 5.36 * 9.81
Mwl = (198 - 186)*0.01
Mdl = (95-62)*0.01
Mtl = (93-62)*0.01
Mlwl = 0.1
Mlhl = (-74 + 167)*0.01
T = 5.12
Lh = (D*Mdl -T *Mtl + Lwf*Mlwl + Macwing - I*topas)/Mlhl
print(Lh)




# %%
Clh = 2*Lh/(1.225 * 20 * 20 * Stail)

# %%
Clh

# %%
effangle = Clh/clalphah
effangle = effangle
alpha = Clto/clalphaw
angle = effangle - (-0.042 + 0.542*alpha)
print(angle)

# %%
(angle)/taue

# %%



