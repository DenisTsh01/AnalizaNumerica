import numpy as np
import matplotlib.pyplot as plt
import math

a3 = -1
b3 = 1
x = np.linspace(a3,b3)

def f3(x):
    return x + np.e**(-x**2)*np.cos(x)

plt.plot(x,f3(x))

def f3prim(x):
    
    return (-np.e**(-x**2))*np.sin(x)-2*x*np.e**(-x**2)*np.cos(x)

plt.plot(x,f3prim(x))

plt.show()

x=0
N=10
TOL = 10**(-8)

def NewtonRaphson(f3,f3prim,x0,TOL):
    while(np.abs(f3(x0)) >= TOL):
            x0=x0-f3(x0)/f3prim(x0)
    return x0




a=0
b=np.pi/2
def f(x):
    return np.cos(x)-x

def fprim(x):
    return -np.sin(x) - 1

n = NewtonRaphson(f,fprim,b,TOL)
print(n)


n = NewtonRaphson(f, fprim, np.pi/4 , TOL)


x_values = np.linspace(a, b)
y_values = f(x_values)
#graficul funcției f(x)
plt.plot(x_values, y_values, label='f(x)')
 
plt.axhline(y=0, linestyle='--', label='y = 0') #y=0

x_aprox = np.array(n)
y_aprox = f(x_aprox)
plt.scatter(x_aprox, y_aprox, color='g', label='aproximari')



plt.legend()
plt.show()
 
 


