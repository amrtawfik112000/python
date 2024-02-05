#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 18:23:24 2022

@author: Amr
"""
from pylab import *
import matplotlib.pyplot as plt
"from matplotlib.colors import LogNorm"
MC = 200
powerT = []
frequencyT = []
runs= range (1,MC)
for run in runs :

    
    x=[]
    y=[]
    c=1
    with open('/home/shahid/Documents/MC/D_KP/tran'+str(run)+'.raw','r') as file:
    # reading each line    
        for line in file:
            if c == 1 :
                c=2
                continue
        
            count=0;
        # reading each word        
            for word in line.split():
   
            # displaying the words 
                if count == 0 :
                    x.append(float(word)) 
                if count == 1 :
                    y.append(float(word)) 
                count =+1 
          
    flag=0
    maxy = max(y)
    TDROP = 0.25*len (x)
    miny = min(y)
    index_X = 0
    index_N =0
    for postion in y :
        if flag ==0 :
            index_X += 1 
        
        if (postion <= 0) &  (y[index_X+1] >= 0)  & (index_X > TDROP) & (flag == 0) :
            flag = 1
            continue
    
    
        index_N += 1 
        if (postion <= 0) &  (y[index_N+1] >= 0)  &  (flag == 1) & (index_N > index_X ):
            break


    frequency = 10**-9/( x[index_N] - x[index_X] ) 

    power = maxy**2*.01

   
    powerT.append(power)
    frequencyT.append(frequency)
    
"""
"""
figure()
plt.hist(frequencyT, bins=MC)  
xlabel("frequency in GHZ")
ylabel("counts")

figure()
plt.hist(powerT, bins=MC)   
 