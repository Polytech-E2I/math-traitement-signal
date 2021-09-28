import numpy as np
import matplotlib.pyplot as plt

T1 = 8
T2 = 2

n = 1000
xmin = -5
xmax = -xmin
t = np.linspace(xmin, xmax, n)
T = t[1] - t[0] # sampling width

f1 = np.where(np.logical_and(t >= -T1/2, t <= T1/2), 1, 0)
f2 = np.where(np.logical_and(t >= -T2/2, t <= T2/2), 1, 0)

tc = np.linspace(xmin, xmax, n)
conv = np.convolve(f1, f2, mode='same') * T # *T to scale the convolution

fig, axis = plt.subplots(1, 1)
axis.plot(t, f1, label=r'$f_1(t)$')# = \Pi(\frac{t}{T_1})$')
axis.plot(t, f2, label=r'$f_2(t)$')# = \Pi(\frac{t}{T_2})$')
axis.plot(tc, conv, label=r'$f_1(t) * f_2(t)$')
axis.legend(loc="best")
axis.grid(True)

axis.set_xlabel("t")
fig.suptitle("Convolution de $f_1$ et $f_2$", fontweight="bold")
fig.canvas.draw()
plt.show()
