import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return (x**3+4*x**2-10)

def phi_1(x):
    return (-x**3-4*x**2+x+10)

def phi_1_derivate(x):
    return (-3*x**2-8*x+1)

def phi_2(x):
    return np.sqrt((10 / x) - 4 * x)

def phi_2_derivate(x):
    return ((-1)*2*x**2*np.sqrt(x)+ 5*np.sqrt(x))/(np.sqrt(10-4*x**2)*x**2)

def phi_3(x):
    return 1/2*np.sqrt(10-x**3)

def  phi_3_derivate(x):
    return (-1)*(3*x**2)/(4*np.sqrt(10-x**3))

def phi_4(x):
        return np.sqrt(10 / (x + 4) )

def phi_4_derivate(x):
    return (-1)*(5*np.sqrt(x+4))/(np.sqrt(10)*(x+4)**2)   

a = 1
b = 2

#(b1)
#(ii) nu verifica ø2

# x_graf1 = np.linspace(a,b)
# y_graf1 =  np.abs(phi_1_derivate(x_graf1))
# plt.plot(x_graf1,y_graf1, label="ø1 deriv")

# x_graf3 = np.linspace(a,b)
# y_graf3 =  np.abs(phi_3_derivate(x_graf3))
# plt.plot(x_graf3,y_graf3, label="ø3 deriv")

x_graf4 = np.linspace(a,b)
y_graf4 =  np.abs(phi_4_derivate(x_graf4))
plt.plot(x_graf4,y_graf4, label="ø4 deriv")

plt.grid()
plt.legend()

plt.show()

# dx_graf = np.linspace(a,b)
# dy_graf = f(dx_graf)
# plt.plot(dx_graf,dy_graf , label="f")

# dx_graf1 = np.linspace(a,b)
# dy_graf1 = phi_1(dx_graf1)
# plt.plot(dx_graf1,dy_graf1,label="ø1")

dx_graf3 = np.linspace(a,b)
dy_graf3 = phi_3(dx_graf3)
plt.plot(dx_graf3,dy_graf3,label="ø3 ")

# dx_graf4 = np.linspace(a,b)
# dy_graf4 = phi_4(dx_graf4)
# plt.plot(dx_graf4,dy_graf4,label="ø4")

plt.grid()
plt.legend()

plt.show()



#(b3) 
def metoda_iterativa_de_pct_fix4(a, b):
    x = 1
    for i in range(b):
        x = phi_4_derivate(x)
        print(f"ø4: {x}, {phi_4(x)}")

metoda_iterativa_de_pct_fix4(1,20)

def metoda_iterativa_de_pct_fix3(a, b):
    x = 1
    for i in range(b):
        x = phi_3_derivate(x)
        print(f"ø3:pasul {i+1}: {x}, {phi_3(x)}")

metoda_iterativa_de_pct_fix3(1,20)

# def metoda_iterativa_de_pct_fix2(a, b):
#     x = 1
#     for i in range(b):
#         x = phi_2_derivate(x)
#         print(x, phi_2(x))

# metoda_iterativa_de_pct_fix2(1,20)

# def metoda_iterativa_de_pct_fix(a, b):
#     x = 1
#     for i in range(b):
#         x = phi_1_derivate(x)
#         print(x, phi_1(x))

# metoda_iterativa_de_pct_fix(1,20)


#(b4)
#phi 3 mai rapid

