import numpy as np
from matplotlib import pyplot as plt


#  - Warm-up - 


# -i-
n = 2468
a4 = np.linspace(0,1,n+1)
dx4 = a4[1] - a4[0]
func4 = a4**5
areas4 = dx4 * func4[:-1]
inleft = sum(areas4)
print(inleft)


# -ii-

nmax = 2467 

for i in range(0,nmax+1):
    z = (0+ 1/2468 * i)**5 * (1/2468)
    
print(z)


# -iii-

# Psuedocodes are to be taken LITERALLY

s = 0
for i in range(0, 2468):
    s = s + (0+ 1/2468 * i)**5 * (1/2468)
print(s)



# -----------------------------------------------------------------# 

# Indefinite Integral 


# Trying to find the indefinite integral of cos(x) using 
# the idea of parameter sweep of riemann sum 

import numpy as np
from matplotlib import pyplot as plt

# function of riemann sum 
def process(x):
    n = 1000
    m = np.linspace(0, x, n+1)
    dx = m[1] - m[0]
    func = np.cos(m)
    areas = dx * func[:-1]
    integral =  sum(areas)
    return integral 

print(process(3 * np.pi/2)) 
    

a = np.linspace(0, 4 * np.pi, 1000)
results = np.zeros(len(a))


for i in range(len(a)):
    results[i] = process(a[i])

fig,ax = plt.subplots()
ax.plot(a, results)

# to check visually as well 
fig,ax = plt.subplots()
ax.plot(a, np.sin(a), color = 'orange')

# Can also calculate the absolute error between two equations 


#--------------------------------------------------------------#

# Calculate Gaussian Curve/ Normal Distribution Curve 

# -1- 

def gaussian(x):
    n= 1000
    s = np.linspace(0, x, n+1)
    dx = s[1] - s[0]
    func = (1/np.sqrt(2 * np.pi)) * np.exp(-s**2 / 2)
    areas = dx * func[:-1]
    integral = sum(areas)
    return integral 

k = np.linspace(0, 10, 1000)
resultg = np.zeros(len(k))

for i in range(len(k)):
    resultg[i] = gaussian(k[i])

fig,ax = plt.subplots()
ax.plot(k, resultg)



# -2- 

def gaussian2(x):
    n= 1000
    s = np.linspace(-x, x, n+1)
    dx = s[1] - s[0]
    func = (1/np.sqrt(2 * np.pi)) * np.exp(-s**2 / 2)
    areas = dx * func[:-1]
    integral = sum(areas)
    return integral 

k = np.linspace(0, 10, 1000)
resultg2 = np.zeros(len(k))

for i in range(len(k)):
    resultg2[i] = 1 - gaussian2(k[i])

ax.plot(k, resultg2)


#---------------------------------------------------------------------#
    