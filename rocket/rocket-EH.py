# -*- coding: utf-8 -*-
"""
Method: Euler-Heun
"""

import numpy as np
import matplotlib.pylab as plt

dm = 1.25
vex = 5
drag = 2.5e-2
g0 = 9.81
r = 6.371e6
grav = g0 * r ** 2


def m(t):
    return 5 - dm * t


def fx(t, x, v):
    return v


def fv(t, x, v):
    return ((dm * vex - dm * v - drag * v ** 2) / m(t)) - grav / (r + x) ** 2


NUMBER_OF_STEPS = 200

x = np.zeros(NUMBER_OF_STEPS)
v = np.zeros(NUMBER_OF_STEPS)
t = np.zeros(NUMBER_OF_STEPS)

x[0] = 0
v[0] = 0
t[0] = 0

h = 0.02

for n in range(1, NUMBER_OF_STEPS):
    K1x = fx(t[n - 1], x[n - 1], v[n - 1])
    K1v = fv(t[n - 1], x[n - 1], v[n - 1])
    K2x = fx(t[n - 1] + h, x[n - 1] + h * K1x, v[n - 1] + h * K1v)
    K2v = fv(t[n - 1] + h, x[n - 1] + h * K1x, v[n - 1] + h * K1v)

    x[n] = x[n - 1] + 0.5 * h * (K1x + K2x)
    v[n] = v[n - 1] + 0.5 * h * (K1v + K2v)
    t[n] = t[n - 1] + h

plt.subplot(211)
plt.plot(t, x)
plt.ylabel('x(m)', rotation=0)
plt.grid()
plt.subplot(212)
plt.plot(t, v)
plt.ylabel('v(m/s)', rotation=0)
plt.grid()


# plt.plot(t, v, "o", t, exact(t))
plt.show()
