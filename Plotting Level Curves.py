import numpy as np
from matplotlib import pyplot as plt


# Plot Level curves 

# Set up the intervals for x and z 
x = np.linspace(-3,3, 100)
z = np.arange(-20,24, 4)

y = np.zeros(len(x))

# Boundaries 
y2 = np.sqrt( 9 - x**2 )
y2neg = -np.sqrt( 9 - x**2 )

fig,ax = plt.subplots()

# Plotting boundaries 
ax.plot(x,y2)
ax.plot(x,y2neg)


# Level curve for the function 
for i in range(len(x)):
    y = np.cbrt(z[i] - x**3)    
    ax.plot(x,y)

# Can use it as a function inside a function 
#--------------------------------------------------------------------------#

# Parameter sweep for geometric series for 1/n 

import numpy as np
from matplotlib import pyplot as plt

# We want to see what values x can be 

parameter = np.linspace(-5, 5, 20)

def geometric(n):
    for i in range(0, len(parameter)):
        y[i] = 1/(2**n)
    return y 

# parameter 


result = np.zeros(len(parameter))

for i in range(len(parameter)):
    result[i] = geometric(parameter[i])

fig,ax = plt.subplots()
ax.scatter(parameter, )
    
    
    








