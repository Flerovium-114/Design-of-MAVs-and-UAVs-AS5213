import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


df=pd.DataFrame(columns=["S.No","W0","We/W0","W0new"])
i = 1
wp = 0.8
wb = 1.25
A=0.76
L= -0.16
w0old = 15
w0new = 0
w0_curr = [w0old]
wef = A*(w0old**L)
iter = [0]

while(True):
    df1=pd.DataFrame({"S.No":i,"W0":w0old,"We/W0":wef,"W0new":w0new},index=[0])
    if(i>2000):
        break

    w0new = (wp + wb) / (1 - wef)
    

    if(abs(w0new-w0old)<0.0001):
        print("Solution Converged with W0 = ",w0new, " After ",i," Iterations")
        break
    else:
        w0old = w0new
        wef = A*pow(w0new,L)
    df=df._append(df1,ignore_index=True)
    i=i+1
    w0_curr.append(w0new)
    iter.append(i)
    #print("wef = ",wef)

#After adding 10% tolerance
print("W0new= ",w0new*1.1)
print("Wef = ",wef)
print("wbf = ", wb/(w0new*1.1))
plt.plot(iter,w0_curr)
plt.xlabel("Number of iterations")
plt.ylabel("DTOW")
plt.title("DTOW vs  Number of iterations")
plt.grid()
plt.show()
