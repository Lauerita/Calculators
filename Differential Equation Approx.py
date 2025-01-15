
# Differential Equation Approximation 

import numpy as np
from matplotlib import pyplot as plt

# y = yk-1 + delta_t(f(yk-1))

# Initialize y0, T, delta_t, and f(y)

delta_t = 0.25
T = 1 
y0 = 1

arraysize = np.arange(0, T + delta_t, delta_t)
y = np.zeros(len(arraysize))

y[0] = y0
fofy = y # you can also try to remake it into a function 



for k in range(1, len(arraysize)):
    y[k] = y[k-1] + delta_t * (fofy[k-1])

# Plot results 
fig, ax = plt.subplots()
ax.plot(arraysize, y, marker = 'o')
ax.plot(arraysize, np.exp(arraysize), marker = 'o')

# ---------------------------------------------------------------#

# Initialize y0, T, delta_t, and f(y)

import numpy as np
from matplotlib import pyplot as plt

delta_t = 0.1
T = 4 
z0 = 3

arraysize = np.arange(0, T + delta_t, delta_t)
z = np.zeros(len(arraysize))

z[0] = z0

def f(z):
    return 1/(z+1)
# Learned that it is the safest to have a function set for the dy/dt 

for k in range(1, len(arraysize)):
    z[k] = z[k-1] + delta_t * f(z[k-1])

z_real = -1 + np.sqrt(16 + 2*arraysize)
    
# Plot results 
fig, ax = plt.subplots()
ax.plot(arraysize, z)
ax.plot(arraysize, z_real)


#--------------------------------------------------------------#


import numpy as np
from matplotlib import pyplot as plt
delta_t = 0.0001
T = 8 
z0 = 7

arraysize = np.arange(0, T + delta_t, delta_t)
z = np.zeros(len(arraysize))

z[0] = z0
def f(z):
    return 2*z*(1-z)


for k in range(1, len(arraysize)):
    z[k] = z[k-1] + delta_t * f(z[k-1])

    
# Plot results 
fig, ax = plt.subplots()
ax.plot(arraysize, z)


#-----------------------------------------------------------#


    


