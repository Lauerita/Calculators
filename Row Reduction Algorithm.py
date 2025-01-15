import numpy as np


A = np.array([[2,4,3,-1], [4,8,1,1], [1,1,1,1]], dtype = float)
a,b = np.shape(A)


# forward substitution 

for j in range(0, a):
    A[j,:] = 1/A[j,j] * A[j,:]
    for i in range(j+1 , a):
        A[i, :] = A[i, :] - A[i,j] * A[j]
        

# backwards substitution 
# using the answers from the very last row 


for k in range(a-1, 0, -1):
    print(k)
    for n in range(0, k):
        A[n,:] = A[n,:] - A[n,k] * A[k,:]
        
        
# Tools for linear algebra in numpy 

np.linalg.solve # solve a system of equations 
np.linalg.norm # length of a vector,1D array 
np.linalg.qr # QR factorization 
np.linalg.eig # eigenvalues 
np.linalg.lstsq # "least square problems"




