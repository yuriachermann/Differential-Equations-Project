# -*- coding: utf-8 -*-
"""
Method: Runge-Kutta
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


h = 0.02
NUMBER_OF_STEPS = 1500

i = np.zeros(NUMBER_OF_STEPS)
a = np.zeros(NUMBER_OF_STEPS)
t = np.zeros(NUMBER_OF_STEPS)
r = np.zeros(NUMBER_OF_STEPS)

i[0] = 0
a[0] = 6
t[0] = 0
r[0] = res(0)


for n in range(1, NUMBER_OF_STEPS):
    K1i = fi(t[n - 1], i[n - 1], a[n - 1])
    K1a = fa(t[n - 1], i[n - 1], a[n - 1])
    K2i = fi(t[n - 1] + h * 0.5, i[n - 1] + h * K1i * 0.5, a[n - 1] + h * K1a * 0.5)
    K2a = fa(t[n - 1] + h * 0.5, i[n - 1] + h * K1i * 0.5, a[n - 1] + h * K1a * 0.5)
    K3i = fi(t[n - 1] + h * 0.5, i[n - 1] + h * K2i * 0.5, a[n - 1] + h * K2a * 0.5)
    K3a = fa(t[n - 1] + h * 0.5, i[n - 1] + h * K2i * 0.5, a[n - 1] + h * K2a * 0.5)
    K4i = fi(t[n - 1] + h, i[n - 1] + h * K3i, a[n - 1] + h * K3a)
    K4a = fa(t[n - 1] + h, i[n - 1] + h * K3i, a[n - 1] + h * K3a)

    i[n] = i[n - 1] + h * (K1i + 2 * K2i + 2 * K3i + K4i) / 6
    a[n] = a[n - 1] + h * (K1a + 2 * K2a + 2 * K3a + K4a) / 6
    t[n] = t[n - 1] + h
    r[n] = res(t[n])


# plt.subplot(311)
# plt.plot(t, i)
# plt.grid()
# plt.ylabel('i', rotation=0)
# plt.subplot(312)
# plt.plot(t, a)
# plt.grid()
# plt.ylabel('di/dt', rotation=0)
# plt.subplot(313)
# plt.plot(t, r)
# plt.grid()
# plt.ylabel('r', rotation=0)

# plt.show()


def data_gen(array, t=0):
    cnt = 0
    while cnt < 1500:
        cnt += 1
        t += 0.02
        yield t, array[n - 1]


def init():
    ax.set_ylim(-0.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,


fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,


ani = animation.FuncAnimation(fig, run, data_gen(i), blit=False, interval=10,
                              repeat=False, init_func=init)
plt.show()