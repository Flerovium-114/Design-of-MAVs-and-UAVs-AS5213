import matplotlib.pyplot as plt
import numpy as np
import math

W = [5.5,2,10,2.7,5.5,4]
b = [1.96 , 1, 3, 1.63, 2.6, 1.2]
l = [1.07, 0.66, 0.74, 1.2, 1.25, 0.91]
s_wing = [0.43,0.14,0.68,0.324,0.43,0.22]
a_top = [0.144, 0.063, 0.482,  0.111, 0.11, 0.045]
a_side = [0.168, 0.054,0.028, 0.128, 0.103, 0.103 ]
s_tail = [0.127,0.03,0.2,0.082,0.1,0.03]
v_cr = [20, 15, 19, 18.05, 15.28, 25.55]



for i in range(len(W)):
    print("W/S = ",9.81*W[i]/s_wing[i])


def s_fus_wet_calc(a1,a2):  
    return 1.7*(a1+a2)

def s_wet_wing_tail_calc(a1,a2): 
    return 2.003*(a1+a2)

def AR_calc(b,s): 
    return b**2/s
 
def R_calc(v,l):                    
    return (1.2 * v*l/1.849)*(10**5) 

def e_calc(ar):
    return 1/(1.05 + 0.007*math.pi*ar) 

def k_calc(e,ar):     
    return 1/(math.pi*e*ar)

def M_calc(v):     
    return v/346.03

def cf_calc(R,M):
    return 0.455/((((math.log10(R)))**2.58)*((1 + 0.144 * (M**2)))**0.65)

def cd0_calc(cf,s_wet,s):
    return cf*s_wet/s

def l_by_d_calc(cd0,k):
    return math.sqrt(1/(4*cd0*k))

s_fus_wet = []
s_wet_wing_tail = []
AR = []
R = []
e = []
k = []
M = []
cf = []
cd0 = []
l_by_d = []
s_wet = []
AR_wet = []
Swet_by_S = []

for i in range(len(b)):

    s_fus_wet_temp = (s_fus_wet_calc(a_top[i],a_side[i]))
    s_fus_wet.append(s_fus_wet_temp)

    s_wet_wing_tail_temp = (s_wet_wing_tail_calc(s_tail[i],s_wing[i]))
    s_wet_wing_tail.append(s_wet_wing_tail_temp)

    s_wet_temp = s_wet_wing_tail_temp + s_fus_wet_temp
    s_wet.append(s_wet_temp)

    AR_temp = (AR_calc(b[i],s_wing[i]))
    AR.append(AR_temp)

    AR_wet_temp = ((b[i])**2)/s_wet_temp
    AR_wet.append(AR_wet_temp)

    R_temp = (R_calc(v_cr[i],l[i]))
    R.append(R_temp)

    M_temp = (M_calc(v_cr[i]))
    M.append(M_temp)

    e_temp = e_calc(AR_temp)
    e.append(e_temp)

    k_temp = k_calc(e_temp,AR_temp)
    k.append(k_temp)

    cf_temp = cf_calc(R_temp,M_temp)
    cf.append(cf_temp)

    cd0_temp = cd0_calc(cf_temp,s_wet_temp,s_wing[i])
    cd0.append(cd0_temp)

    Swet_by_S_temp = s_wet_temp/s_wing[i]
    Swet_by_S.append(Swet_by_S_temp)

    l_by_d_temp = l_by_d_calc(cd0_temp,k_temp)
    l_by_d.append(l_by_d_temp)


print("AR = ",AR)
print("AR_wet = ",AR_wet)
print("k = ",k)
print("e = ",e)
print("cd0 = ",cd0)
print("S_wing = ",s_wing)
print("S_wet = ",s_wet)
print("l/d = ",l_by_d)
print("Swet/S = ", Swet_by_S)
print("S = ",s_wing)
print("cf = ",cf)

sqr_AR_wet = []
p = 0

for i in range(len(b)):
    sqr_AR_wet.append(math.sqrt(AR_wet[i]))
    p += Swet_by_S[i]

Swet_by_S_avg = p/len(b)

print("S_wet/S Avg = ",Swet_by_S_avg)




# Convert numbers to strings and format as LaTeX-style expressions
sq_ar_labels = [f'$\\sqrt{{{num:.2f}}}$' for num in sqr_AR_wet]
l_d_labels = [f'$(L/D)_{{max}} = {num:.2f}$' for num in l_by_d]

# Linear regression
regression_coefficients = np.polyfit(sqr_AR_wet, l_by_d, 1)
regression_line = np.polyval(regression_coefficients, sqr_AR_wet)

# Print the equation of the line
equation_of_line = f"$(L/D)_{{max}} = {regression_coefficients[0]:.2f} \\cdot \\sqrt{{AR_{{wet}}}} + {regression_coefficients[1]:.2f}$"
print("Equation of the line:", equation_of_line)

plt.plot(sqr_AR_wet, l_by_d, 'o', label='Data points')
plt.plot(sqr_AR_wet, regression_line, label='Linear Regression')

plt.ylabel("$(L/D)_{max}$")
plt.xlabel("$\\sqrt{AR_{{wet}}}$")  # Update the label
plt.title("$(L/D)_{max}$ vs $\\sqrt{AR_{{wet}}}$")  # Update the title
plt.grid()
plt.text(1.9, 17, equation_of_line, fontsize=10, verticalalignment='bottom', horizontalalignment='right')
plt.legend()
#plt.show()


AR_our = 8
b_our = 2.5
s_wing_our = 0.78
v_our = 20

s_wet_our = 3.674 * s_wing_our
AR_wet_our = b_our**2/s_wet_our

print("AR_wet_our = ", AR_wet_our)
l_by_d_our = 9.89*math.sqrt(AR_wet_our) + 3.22

print("l/d _ our = ",l_by_d_our)

T_W = 1/l_by_d_our

T_cr = T_W * 7.826 * 9.81

print("T_W = ",T_W)
print("T_cr= ", T_cr)

P_cr_our = T_cr * v_our
print("P_cr_our = ", P_cr_our)


M_our = M_calc(v_our)






    


