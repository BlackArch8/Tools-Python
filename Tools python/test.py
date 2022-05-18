
import numpy as np
def f(x):
    f = np.exp(-x)-x
    return f
def bisection(a, b):
    eps = 0.05
    while (eps >= 0.001):
        c=(a+b)/2.0
        if (f(c)*f(a) > 0.0):
          a = c
        else:
          b = c
        eps =  abs(a-b)/a
    return c

print (bisection(0,1))
