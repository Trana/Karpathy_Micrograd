import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 3*x**2 - 4*x + 5


# print(f(3.0))

xs = np.arange(-5, 5, 0.25)

# print(xs)
# ys = f(xs)
# print(ys)

# plt.plot(xs, ys)
# plt.show()

# Derivative example
h = 0.000001 # represents h going to the limit, but here we just set it really small for approximation
x = -3.0 # at 2/3 the slop is zero
# print(f(x)) # 20.0
# print(f(x + h))  # 20.014003000000002
# print(f(x + h) - f(x))  # 0.014003000000002092
# print((f(x + h) - f(x))/h)  # normalized rate of change to get the slope, this is the derivation function


# More complex example
h = 0.000001 

#inputs
a = 2.0
b = -3.0
c = 10.0

#derivative of d with respect to a,b,c
d1 = a*b + c
a += h
d2 = a*b + c

print('d1', d1)
print('d2', d2)
print('slope', (d2 - d1)/h)