#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:36:43 2023

@author: xinyihu
"""

import numpy as np
from matplotlib import pyplot as plt


#  - Warm Up - 


a = np.arange(0,301,1)
D = np.zeros(len(a))

for k in range(len(a)):
    D[k] = np.cos(a[k])

#print(D)
    

# -2- 
sumofD = sum(D)
#print(sumofD)


# -3-
def trigfun(n):
    a1 = np.arange(0,n+1,1)
    D1 = np.zeros(len(a1))
    for i in range(len(a1)):
        D1[i] = np.cos(a1[i])
    return sum(D1)

#print(trigfun(0), trigfun(2), trigfun(4))


# -4- 

# Set up Function 

def power(k):
    n1 = np.zeros(k+1)
    for j in range(1,k+1,1):
        n1[j] = 2**j    
    D2 = np.zeros(len(n1))
    for l in range(len(n1)):
        D2[l] = trigfun(n1[l])
    return n1, D2


n1, sumd2 = power(20)

# Visualization of the graph 

#fig,ax = plt.subplots()
#ax.plot(n1,sumd2, marker = 'o')

#plt.rcParams.update({'font.size': 10})

#ax.set(xlabel = "power index n",
       #ylabel = "partial sum",
       #xscale = "log") # Scale the graph using log to bettwe visualize the graph 
    

    
# ----------------------------------------------------------------------------------- #  

# Numerical Integration 

# Reimann Sum of sin(x) going from 0 to 2pi 

n = 100000

# Left hand side 

x = np.linspace(0, 1, n + 1)

dx = x[1] - x[0] # width since it is the same every time 

func_val = x**2 + 1

areas = dx * func_val[:-1] 

integral = sum(areas)

print(integral)

# Right hand side 

x2 = np.linspace(0, 1, n)

dx2 = x2[1] - x2[0]

areas2 = dx2 * func_val[1:]

integral2 = sum(areas2)

#print(integral2)

# -----------------------------------------------------------------------------------# 

n = 70001

# Left hand side 

x = np.linspace(-1000000, 1000000, n + 1)

dx = x[1] - x[0] # width since it is the same every time 

func_val = np.sin(x)/x

areas = dx * func_val[:-1] 

integral = sum(areas)

print(integral)

# Right hand side 

x2 = np.linspace(0, 1, n)

dx2 = x2[1] - x2[0]

areas2 = dx2 * func_val[1:]

integral2 = sum(areas2)

#print(integral2)


def integral(a,b,n):
    x_left = np.linspace(a, b, n+1)
    x_right = np.linspace(a,b,n)
    
    dx_left = x_left[1] - x_left[0]
    dx_right = x_right[1] - x_right[0]
    
    func_vals_left = x_left** 2 + 1
    func_vals_right = x_right** 2 + 1
    
    area_left = dx_left * func_vals_left[:-1]
    area_right = dx_right * func_vals_right[1:]
    
    area_left_sum = sum(area_left)
    area_right_sum = sum(area_right)
    
    return area_left_sum, area_right_sum, (area_left_sum + area_right_sum)/2

area_left_sum, area_right_sum, avg  = integral(0,3,1000)
print(area_left_sum, area_right_sum, avg)




















     
    