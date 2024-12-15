import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

W = [5.5,2.2,2,2.7,5.5,4,10,22]
EW = [2.4,1.82,1.72,1.7,2.8,2,4.4,14]
EWF = []
for i in range(len(W)):
    EWF.append(EW[i]/W[i])

log_EWF = np.log(EWF)
log_W = np.log(W)


coefficients = np.polyfit(log_W, log_EWF, 1)
line = np.polyval(coefficients, log_W)


slope = coefficients[0]
intercept = coefficients[1]

#print("L = ",slope)
#print("A = ",math.exp(intercept))


plt.plot([math.log(x) for x in W], [math.log(x) for x in EWF],'bo')
plt.plot(log_W, line, label='Fitted Line')
plt.ylabel('log(EW/W)')
plt.xlabel('log(W)')
plt.title('Logarithmic plot of EW/W against W')
plt.grid()
plt.show()

A = 0.76
L = -0.16

Wl=[]
Wexp=[]
x1=[]
for i in range(25):
    x1.append((i+1))
    Wexp.append(A*math.pow((i+1),L))
for num in W:
    Wl.append(math.log(num))
x=W
y=EWF

for weight in range(len(Wl)):
    y[weight] = math.exp(log_EWF[weight])
plt.plot(x,y,'o',x1,Wexp,'-')
plt.title("Empty weight fraction vs DTOW")
plt.legend(["data points","best fit curve"])
plt.xlabel("DTOW")
plt.ylabel("Empty Weight Fraction")
plt.grid()
plt.show()

def cl(w0,v):
    return (w0*9.81)/(0.6*(v**2)*0.78)

def cd(cl):
    return 0.04 + 0.047*(cl**2)



df=pd.DataFrame(columns=["S.No","W0","We/W0","W0new"])
wp=1.15
wc = 0

w0old = 12

w0new = 0
i=1
A=0.76
L= -0.16
wef = A*(w0old**L)
#print("wef = ",wef)


s = 0.78
v_cr = 20
t_cr = 117*60
t_climb = 60

w0_curr = [w0old]
iter = [0]

energy = 0

while(True):
    df1=pd.DataFrame({"S.No":i,"W0":w0old,"We/W0":wef,"W0new":w0new},index=[0])
    if(i>2000):
        break

    v_climb = 4.27*(w0old**0.5)
    cl_old = cl(w0old,v_cr)
    cl_climb = cl(w0old,v_climb)
    

    D_cr = cd(cl_old)*0.6*(v_cr**2)*s
    D_climb = cd(cl_climb)*0.6*(v_climb**2)*s

    P_cr = D_cr*v_cr
    P_climb = D_climb*v_climb
    E_ground = (1.21 * ((w0old*9.81)**2))/(9.81*1.225*1.62*s)*2
    P_loiter = 1612.41*1.7 * (0.04 + 0.000522 * (w0old**2))

    #print("P_loiter =",P_loiter)
    #print("P_cruise = ", P_cr)
    #print("P_climb = ", P_climb)
   
    E_cr = P_cr * t_cr*0.1
    E_climb = P_climb*t_climb*2
    E_loiter = P_loiter*t_cr*0.9

    #print("E_climb = ", E_climb)
    #print("E_loiter = ", E_loiter)
    #print("E_cr = ",E_cr)
    #print("E_ground = ", E_ground)

    E = E_cr + E_loiter + E_ground + E_climb
    
    
    wb = 1.33*E*0.000278/300
    #print("wb/w0old = ",wb/w0old)

    w0new = (wp+wc)/(1-(wb/w0old)-wef) 
    # print("Iteration ",i,"done")
    # print(wef,w0new,w0old)
    if(abs(w0new-w0old)<0.01):
        print("Solution Converged with W0 = ",w0new, " After ",i," Iterations")
        break
    else:
        w0old = w0new
        wef = A*pow(w0new,L)
    df=df._append(df1,ignore_index=True)
    i=i+1
    #print("wef = ",wef)
    #print("w0new = ",w0new)
    w0_curr.append(w0new)
    iter.append(i)

print("Energy = ",E)  
print("wb = ",wb)
print("wef = ",wef)
print("w0new = ",w0new)
print("wb/w0old = ",wb/w0old)
    
plt.plot(iter,w0_curr)
plt.xlabel("Number of iterations")
plt.ylabel("DTOW")
plt.title("DTOW vs  Number of iterations")
plt.grid()
plt.show()

print("cl = ",cl(w0new,v_cr))
print("E",E)
print("wb/w0 = ",wb/w0new)
print("cd = ",cd(cl(w0new,v_cr)))
df.astype({"S.No":int})


print(df.dtypes)
df.to_latex("Weight_Calc.tex",index=False)

print(df)


