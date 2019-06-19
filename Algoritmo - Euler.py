# -*- coding: utf-8 -*-
"""
Descrição: Método de Euler para 1 equação de 1a Ordem
@author: Prof. Diogo Nardelli Siebert
"""

import numpy as np
import matplotlib.pylab as plt


def exact(t):
    return t / 4. - 3. / 16. + 19. * np.exp(4 * t) / 16.


def f(t, y):
    return 1 - t + 4 * y


NUMBER_OF_STEPS = 10
y = np.zeros(NUMBER_OF_STEPS)
t = np.zeros(NUMBER_OF_STEPS)

y[0] = 1
t[0] = 0

h = 0.02

for n in range(1, NUMBER_OF_STEPS):
    K1 = f(t[n - 1], y[n - 1])
    y[n] = y[n - 1] + K1 * h
    t[n] = t[n - 1] + h

plt.plot(t, y, "o", t, exact(t))
plt.show()
