import numpy as np

# Develope an algorithm to calculate the greatest common divisor 

#-------------------------------#

# Following an example step by step 

def euclidean(a, b):
    # for this to work a > b
    q1 = a//b
    r1 = a - b*q1
    q2 = b//r1
    r2 = b - q2 * r1 
    q3 = r1//r2
    r3 = r1 - r2 * q3
    
    return q3, r3
    
print(euclidean(2415, 945))


#-------------------------------#


# Automated 

def euclidean_auto(a, b):
    r = np.zeros(100)
    q = np.zeros(100)
    q[0] = a//b
    r[0] = a - b*q[0]
    q[1] = b//r[0]
    r[1] = b - q[1] * r[0]
    if r[1] == 0:
        return r[0]
    for i in range(2, len(r)):
        q[i] = r[i-2]//r[i-1]
        r[i] = r[i-2] - r[i-1] * q[i]
        if r[i] == 0:
            return r[i-1], i

        
print(euclidean_auto(13432, 471))       

        
        