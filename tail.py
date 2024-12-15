s = [0.286, 2.048, 0.692, 0.63]
s_ht = [0.046, 0.402, 0.123, 0.106]
l_ht = [0.667, 1.577, 1.321, 1.171]  #MAC of wing to MAC of H tail
c_ht = [0.45, 0.271, 0.185, 0.1505]
b_ht = [0.1005, 1.459, 0.675, 0.695]    # Raven B, PUMA LE, Skylark, FT100
b = [1.4, 4.6, 2.4, 2.7]
c = [0.2, 0.4715, 0.273, 0.208]
s_v = [0.015, 0.092, 0.085, 0.045]
l_v = [0.54, 1.45, 1.25, 1.171]

AR_ht_our = 16/3

vh = []
AR_w = []
AR_t1 = []
AR_t2 = []
vv = []

num = len(s)

for i in range(num):
    vh.append(l_ht[i]*s_ht[i]/(c[i]*s[i]))
    AR_w.append(b[i]**2/s[i])
    AR_t1.append(b_ht[i]**2/s_ht[i])
    AR_t2.append(b_ht[i]/c_ht[i])
    vv.append(l_v[i]*s_v[i]/(c[i]*s[i]))
   
print("AR_w: ",AR_w)
print("AR_t_1: ",AR_t1)
print("AR_t_2: ",AR_t2)
print("vh: ",vh)
print("vv: ",vv)

print("avg vh: ",sum(vh)/num)
print("avg_l_ht: ", sum(l_ht)/num)
print("avg_vv; ", sum(vv)/num)
print("avg_lv; ", sum(l_v)/num)

