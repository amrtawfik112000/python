#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:18:17 2024

@author: Amr
"""
from pylab import *
import matplotlib.pyplot as plt
    
VGS=[]
ID=[]
gm=[]
gm_gds=[]
gds=[]
Vov=[]
Vstar=[]
gm_ID = []
VTH = 0.783

#read gm
with open("/home/Amr/Analog/simulation/gm.raw",'r') as file:
    
    # reading each line    
    for line in file:
        # reading each word 
        VGS_val , gm_val = line.split(None,2)
        VGS.append(float(VGS_val))
        gm.append(float(gm_val))
        Vov.append(float(VGS_val)-VTH)
#read gds
with open("/home/Amr/Analog/simulation/gds.raw",'r') as file:
    
    # reading each line    
    for line in file:
        # reading each word 
        VGS_val , gds_val = line.split(None,2)
        gds.append(float(gds_val))

#read ID
with open("/home/Amr/Analog/simulation/ID.raw",'r') as file:
    
    # reading each line    
    for line in file:
        # reading each word 
        VGS_val , ID_val = line.split(None,2)
        ID.append(float(ID_val))


Vstar = [2*id/GM for id,GM in zip(ID,gm)]


figure() 
plot(VGS,Vov)
plot(VGS,Vstar)
xlabel('VGS')
ylabel('Vstar & Vov')

figure()
plot(VGS,gm)
xlabel('VGS')
ylabel('gm')

figure()
plot(VGS,ID)
xlabel('VGS')
ylabel('ID')

figure()
plot(VGS,gds)
xlabel('VGS')
ylabel(' gds')

