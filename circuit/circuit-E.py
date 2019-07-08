# -*- coding: utf-8 -*-
"""
Method: Euler
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

c = 1
l = 1


def res(t):
    return 5 + 1.2 * np.sin(t)


def fi(t, i, a):
    return a


def fa(t, i, a):
    return -(res(t) * a / l) - (i / (l * c))


h = 0.01
NUMBER_OF_STEPS = 3000

i = np.zeros(NUMBER_OF_STEPS)
a = np.zeros(NUMBER_OF_STEPS)
t = np.zeros(NUMBER_OF_STEPS)

i[0] = 0
a[0] = 6
t[0] = 0


for n in range(1, NUMBER_OF_STEPS):
    K1i = fi(t[n - 1], i[n - 1], a[n - 1])
    K1a = fa(t[n - 1], i[n - 1], a[n - 1])

    i[n] = i[n - 1] + h * K1i
    a[n] = a[n - 1] + h * K1a
    t[n] = t[n - 1] + h

plt.subplot(211)
plt.plot(t, i)
plt.grid()
plt.ylabel('i', rotation=0)
plt.subplot(212)
plt.plot(t, a)
plt.grid()
plt.ylabel('di/dt', rotation=0)

plt.show()
