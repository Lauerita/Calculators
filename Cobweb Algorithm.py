import numpy as np
import matplotlib.pyplot as plt

# cobweb plotting 

x = np.linspace(-10, 10, 10000)# controlled step sizes

# set up functions 

def func1(x): #orbit function
    y = (3*x - x**3)/2
    return(y)

def func2(x): #linear function 
    y = x
    return(y)


y1 = func1(x)
y2 = func2(x)

fig,ax = plt.subplots()
ax.axhline(y = 0, color = 'black')
ax.axvline(x = 0, color = 'black')
ax.set(xlabel = 'x',
       ylabel = 'y')
ax.set_xlim(-2,2) #scale of the plot
ax.set_ylim(-2,2) #scale of the plot
ax.plot(x, y1)
ax.plot(x, y2)
 

x_val = np.zeros(1000) #set up storage for iterations
y_val = np.zeros(1000)  

x0 = 1.6 # initial condition
x_val[0] = x0
x_val[1] = x_val[0]
y_val[1] = func1(x_val[1])


for i in range(2, len(x_val)):
    if np.mod(i,2) == 0:
        y_val[i] = y_val[i-1]
        x_val[i] = func2(y_val[i])
    else:
        x_val[i] = x_val[i-1]
        y_val[i] = func1(x_val[i])

    
ax.plot(x_val ,y_val, color = 'green', marker = '.')

