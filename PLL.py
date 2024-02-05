# -*- coding: utf-8 -*-
"""
Spyder Editor

written by : Amr Tawfik Mostafa
email : amrtawfik112000@gmail.com

"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal



pi=3.14

Icp = 100e-6; Kvco = 2*pi*600e6; M = 64;
R1 = 6.5e3; C1 = 100e-12; C2 = C1/10;

# Open Loop Gain:
wz = 1 / (R1*C1)
w_ugb = wz * np.sqrt((C1/C2)+1);
wp3 = (C1 + C2) / (R1*C1*C2);
PM_Max = (np.arctan(w_ugb/wz) - np.arctan(w_ugb/wp3)) *360/(2*pi)
Const1 = (Icp*Kvco)/(2*pi*M*C1*C2*R1)

def get_gain_Bw_UGF(num, den):
    sys = signal.TransferFunction(num, den)
    w, mag, phase = signal.bode(sys)
    
    Bw = w[(np.abs(mag-mag[0] +3)).argmin()]
    UGF = w[(np.abs(mag )).argmin()]
    PM = 180 + phase[(np.abs(mag )).argmin()]
    return  Bw, UGF ,w , mag , phase , PM



num = [C1*R1*Const1 , Const1]  
den = [1 , ((C1+C2)/(C1*C2*R1)) , 0 , 0]

Bw, UGF , w , mag , phase , PM  = get_gain_Bw_UGF(num, den)

plt.subplot(2,1,1)
plt.semilogx(w,mag)
plt.subplot(2,1,2)
plt.semilogx(w,phase)


[z,p,k] = signal.tf2zpk(num,den)


#-------------------------------------------------------
# Closed Loop Gain:
    
num_CL =  [(C1*R1*Const1*M) , (M*Const1)]
den_CL =[1 , ((C1+C2)/(C1*C2*R1)) , (C1*R1*Const1) ]

Bw_CL, UGF_CL , w_CL , mag_CL , phase_CL , PM_dummy  = get_gain_Bw_UGF(num_CL , den_CL)



fz = wz / (2*pi)
fp = wp3 / (2*pi)
fc = UGF / (2*pi)
print('---------------------')
print('Bw = ' , Bw)
print('UGF =' , UGF)
print('PM_Max =' , PM_Max)
print('phase margin =' , PM)
print('---------------------')
print('Fz =' , fz)
print('Fp =' , fp)
print('Fc =' , fc)
print('---------------------')
print('poles' , p)
print('zores' , z)



