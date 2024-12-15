import math
rho = 1.2
mu = 1.85 * (10**-5) 
v = 20
l = [0.23, 1.69, 0.1137, 0.1198]       # wing, fus, ht, vt

Re = []
cf_lam = []
cf_tur = []
K_lam = [0.4, 0.25, 0.4, 0.4]
cf = []
Q = [1 , 1, 1.04, 1.04]
Swet = [0.861, 0.6295, 0.1405, 0.075115]
FF = [1.012, 1.4114, 1.012, 1.012]
Sref = 0.42
cd = 0

for i in range(len(l)):
    Re_temp = rho*v*l[i]/mu
    Re.append(Re_temp)
    cf_lam_temp = (1.328/math.sqrt(Re_temp))
    cf_tur_temp = 0.455/(math.log10(Re_temp)**2.58)
    cf_tur.append(cf_tur_temp)
    cf_lam.append(cf_lam_temp)
    cf_temp = cf_lam_temp*K_lam[i] + cf_tur_temp*(1 - K_lam[i])
    cf.append(cf_temp)
    cd += cf_temp*FF[i]*Q[i]*Swet[i]/Sref

print("Re: ", Re)
print("cf_lam: ", cf_lam)
print("cf_tur: ", cf_tur)
print("cf: ", cf)
print("cd: ", cd)

