
import numpy as np
from matplotlib import pyplot as plt


# Sequences and Series + Parameter sweep 

###################################################################

# Fibonacci Sequence 

# 1,1,2,3,5,8,13...

# print the n-th term of the fibo sequence

if False:
    def fibo(b, n = 100):
        a = np.zeros(n)
        a[0] = 1
        a[1] = 1

        for i in range(2, len(a)):
            a[i] = a[i-1] + a[i-2]
            
        print(a[b])    
        return 

#-----------------------------------------------------------#

# Calculate any sequence to the infinite term and determine

# if the sequence converges for diverges 

# Concept used: Function inside a function and recursive 


def function(n):
    return np.exp(5*n)/(4 + np.exp(2*n))

def sequence(func, n = 100000, b = 0, c = 2, d = 4):
    '''
    input:
        a -> testing function, needs to be a function with b as input 

        n -> Optional, default number is 100000, can be changed
        b -> Optional, starting value of the sequence
        c -> Optional, measuring parameter 
        d -> Optional, last (d-1) digits of the sequence
        
    output: 
        The last (d-1) digitals of the sequence 
    '''
    a = np.zeros(n)
    for i in range(n):
        b = b + 1 # not good enough for series but works for sequence 
        a[i] = func(b)
    if abs(a[n-1]) - abs(a[n-c]) <= 0.000001:
        print("Yes, the sequence converges!")
    else:
        print("No, the sequence diverges!")
        
    return a[n-1:n-d:-1]


#-----------------------------------------------------------#

# Calculating sum of any series 

def function(n):
    return 5/np.sqrt(n) - 5/np.sqrt(n + 1)
    

def series_cal(function, a, N = 1000000 ):
    '''
    input: 
        function -> the series you want to calculate 
        a -> starting term 
        N -> ending term, optional 
    output:
        sum -> sum of your series from starting to ending term 

    '''
    sum = function(a)
    for i in range(a + 1, N):
        #print(i)
        sum = sum + function(i)
    return sum 


###################################################################

# Find the radius of convergence using parameter sweep 

# First set-up the pre-defined series 

def series(x, N = 100):
    summ = np.zeros(N)
    summ[0] = 0
    for i in range(1, N):
        summ[i] = + ((-1)**i)*i/4**i * (x + 3)**i + summ[i-1]
    print(summ)
    return abs(summ[-1]) - abs(summ[-2])

# Using the difference between the last two sums based on the definition
# deifnition says that the sum has to be consistent 
# in order for the series to converge 

# range of parameter

a = np.linspace(-10, 10, 100) #<<<<<< Can be tuned ! 

# set up storage for results

result = np.zeros(len(a))        

for i in range(len(a)):
    result[i] = series(a[i])

fig,ax = plt.subplots()
ax.scatter(a, result)
#ax.set_xlim(14/8, 19/8)
ax.set_ylim(0, 0.5)

#-----------------------------------------------------------#

# Question on the midterm 

# z[k] = z[k-1] + 1/m * z[k-1]; k = 1,2,...,m

import numpy as np
from matplotlib import pyplot as plt 

def expo(m):
    z = np.zeros(m)
    z[0] = 1
    for k in range(1, len(z)):
        z[k] = z[k-1] + 1/m * z[k-1]
    return z[-1]

a = np.arange(1, 501)
result = np.zeros(len(a))

for i in range(len(a)):
    result[i] = expo(a[i])

fig,ax = plt.subplots()
ax.scatter(a, result)
    
        
###################################################################


