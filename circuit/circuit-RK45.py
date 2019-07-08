# -*- coding: utf-8 -*-
"""
Method: Runge-Kutta-Fehlberg
"""

import numpy as np
import matplotlib.pyplot as plt

c = 1
l = 1

def r(t):
    return 2 * 1.2 * np.sqrt(l / c) + 1.2 * np.sin(t)


def fi(t, i, a):
    return a


def fa(t, i, a):
    return -(r(t) * a / l) - (i / (l * c))


h = 0.01
NUMBER_OF_STEPS = 3000

i = np.zeros(NUMBER_OF_STEPS)
a = np.zeros(NUMBER_OF_STEPS)
t = np.zeros(NUMBER_OF_STEPS)

i[0] = 0
a[0] = 6
t[0] = 0

tol = 0.005


def k3(k1, k2):
    return (3 * k1 + 9 * k2) / 32


def k4(k1, k2, k3):
    return (1932 * k1 - 7200 * k2 + 7296 * k3) / 2197


def k5(k1, k2, k3, k4):
    return (439 * k1 / 216) - (8 * k2) + (3680 * k3 / 513) - (845 * k4 / 4104)


def k6(k1, k2, k3, k4, k5):
    return - (8 * k1 / 27) + (2 * k2) - (3544 * k3 / 2565) + (1859 * k4 / 4104) - (11 * k5 / 40)


for n in range(1, NUMBER_OF_STEPS):
    K1i = fi(t[n - 1], i[n - 1], a[n - 1])
    K1a = fa(t[n - 1], i[n - 1], a[n - 1])
    K2i = fi(t[n - 1] + h / 4, i[n - 1] + h * K1i / 4, a[n - 1] + h * K1a / 4)
    K2a = fa(t[n - 1] + h / 4, i[n - 1] + h * K1i / 4, a[n - 1] + h * K1a / 4)
    K3i = fi(t[n - 1] + 3 * h / 8, i[n - 1] + h * k3(K1i, K2i), a[n - 1] + h * k3(K1a, K2a))
    K3a = fa(t[n - 1] + 3 * h / 8, i[n - 1] + h * k3(K1i, K2i), a[n - 1] + h * k3(K1a, K2a))
    K4i = fi(t[n - 1] + 12 * h / 13, i[n - 1] + h * k4(K1i, K2i, K3i), a[n - 1] + h * k4(K1a, K2a, K3a))
    K4a = fa(t[n - 1] + 12 * h / 13, i[n - 1] + h * k4(K1i, K2i, K3i), a[n - 1] + h * k4(K1a, K2a, K3a))
    K5i = fi(t[n - 1] + h, i[n - 1] + h * k5(K1i, K2i, K3i, K4i), a[n - 1] + h * k5(K1a, K2a, K3a, K4a))
    K5a = fa(t[n - 1] + h, i[n - 1] + h * k5(K1i, K2i, K3i, K4i), a[n - 1] + h * k5(K1a, K2a, K3a, K4a))
    K6i = fi(t[n - 1] + h / 2, i[n - 1] + h * k6(K1i, K2i, K3i, K4i, K5i), a[n - 1] + h * k6(K1a, K2a, K3a, K4a, K5a))
    K6a = fa(t[n - 1] + h / 2, i[n - 1] + h * k6(K1i, K2i, K3i, K4i, K5i), a[n - 1] + h * k6(K1a, K2a, K3a, K4a, K5a))

    i4 = i[n - 1] + h * ((25 * K1i / 216) + (1408 * K3i / 2565) + (2197 * K4i / 4104) - (K5i / 5))
    i5 = i[n - 1] + h * ((16 * K1i / 135) + (6656 * K3i / 12825) + (28561 * K4i / 56430) - (9 * K5i / 50) + (2 * K6i / 55))

    a4 = a[n - 1] + h * ((25 * K1a / 216) + (1408 * K3a / 2565) + (2197 * K4a / 4104) - (K5a / 5))
    a5 = a[n - 1] + h * ((16 * K1a / 135) + (6656 * K3a / 12825) + (28561 * K4a / 56430) - (9 * K5a / 50) + (2 * K6a / 55))

    s = ((tol * h) / (2 * abs(i5 - i4))) ** 0.25
    h = s * h

    if 0 == 0:
        print(i4, i5, s)

    if 0 == 0:
        i[n] = i[n - 1] + h * (K1i + 2 * K2i + 2 * K3i + K4i) / 6
        a[n] = a[n - 1] + h * (K1a + 2 * K2a + 2 * K3a + K4a) / 6
        t[n] = t[n - 1] + h
    else:
        n = n - 1


plt.subplot(211)
plt.plot(t, i)
plt.grid()
plt.ylabel('i', rotation=0)
plt.subplot(212)
plt.plot(t, a)
plt.grid()
plt.ylabel('di/dt', rotation=0)

plt.show()
