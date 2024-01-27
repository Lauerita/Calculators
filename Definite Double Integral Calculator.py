import numpy as np
from matplotlib import pyplot as plt

# Algorithm to calculate double integral using the idea of Riemann Sum 

# rectangle division  
i = 1000

# lower and upperbounds of x 
a = 1
b = 4

# lower and upperbounds of y 
c = 1
d = 4


# ste up the divisions on both x and y 
x = np.linspace(a, b, i )
y = np.linspace(c, d, i )

dt = x[1] - x[0]

dt = x[1] - x[0]

# fuction for integration  
def f(x,y):
    '''
    Input: x,y are vector values 
    Output: z, another vector based on the inputs 
    Purpose: Calculate the z = x**2 + y   
    '''
    z = x**2 + y
    return z


# create a matrix that stores all the x values and y values 
storage = np.zeros((len(x)-1, len(y) -1)) 

# storage the sums
rectan = np.zeros(len(x)-1)


    
for k in range(1, i):
            
    for n in range(1, i):   
        storage[n-1, k-1] = f(x[n], y[k])

for a in range(len(x)-1):
    rectan[a] = sum(storage[a, :]) * dt**2

print(sum(rectan))          
            




     

    
    

    

    

    
    
    


