#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:26:48 2023

@author: xinyihu
"""
import numpy as np
from matplotlib import pyplot as plt
    
# Cobweb algorithm 
# The goal is to investigate the trend of the sequence 

# Make a function of the function 

    
def g(v):
    Loan = np.exp(-v)
    return Loan

# Make storage for the cobwebs 
f0 = 1
nmax = 25 # number of iternation 

x = np.zeros(2*nmax) 
y = np.zeros(2*nmax)


# 3 Starting point 
# for f0 = 50000, the horizontal value is 50000, and vertical value is 0 
x[0] = f0
x[1] = f0
y[0] = 0
y[1] = g(f0)


for n in range(1, nmax):
    idx = 2*(n-1)+1 #index of previous yvalue 
    v = y[idx] #previous values 
    x[2*n] = v
    y[2*n] = v
    print(x[n], y[n])
    # 
    x[2*n +1] = v
    y[2*n +1] = g(v)
    print(x[n], y[n])

fig,ax = plt.subplots()
ax.plot(x,y,marker = "o")
# Draw lines 
line1 = np.linspace(0, 6*f0, 500)
ax.plot(line1, line1, color = "red")
ax.plot(line1, g(line1), color = "black")