def bisectie(f, a, b, ITMAX, TOL, OPT=1):
    n = 0
    an, bn = a, b
    xn = 0
    while n < ITMAX:
        xn = an + (bn - an) / 2
        
        if OPT == 1:
            if abs(bn - an) <= TOL:
                return xn, n
            
        elif OPT == 2:
            if n > 0 and abs(xn - xn_1) <= TOL:
                return xn, n
            
        elif OPT == 3:
            if abs(f(xn)) <= TOL:
                return xn, n

        if f(an) * f(xn) <= 0: #verif
            bn = xn
        else:
            an = xn

        xn_1 = xn
        n += 1

    return xn, n


#b)
a = 1
b = 2

ITMAX = 10**4
TOL = 1e-8


def f(x):
    return x**2 - 3


#criteriu 1 
xn, num_iter1 = bisectie(f, a, b, ITMAX, TOL, OPT=1)
print(f"1: rez= {xn}, it: {num_iter1}")

# criteriu 2
xn, num_iter2 = bisectie(f, a, b, ITMAX, TOL, OPT=2)
print(f"2:  rez= {xn}, it:{num_iter2}")

# criteriu 3 
xn, num_iter3 = bisectie(f, a, b, ITMAX, TOL, OPT=3)
print(f"3:  rez = {xn}, it:{num_iter3}")
