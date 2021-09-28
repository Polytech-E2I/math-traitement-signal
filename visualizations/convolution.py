import numpy as np
import matplotlib.pyplot as plt

T1 = 8
T2 = 2

n = 1000
xmin = -5
xmax = -xmin
t = np.linspace(xmin, xmax, n)
T = t[1] - t[0] # sampling width

rect1 = np.where(np.logical_and(t >= -T1/2, t <= T1/2), 1, 0)
rect2 = np.where(np.logical_and(t >= -T2/2, t <= T2/2), 1, 0)

tc = np.linspace(xmin, xmax, 2*n-1)
conv = np.convolve(rect1, rect2, mode='full') * T # *T to scale the convolution

fig, axis = plt.subplots(1, 1)
axis.plot(t, rect1, label=r'$\Pi(\frac{t}{T_1})$')
axis.plot(t, rect2, label=r'$\Pi(\frac{t}{T_2})$')
axis.plot(tc, conv, label=r'$\Pi(\frac{t}{T_1}) * \Pi(\frac{t}{T_1})$')
axis.legend(loc="best")
axis.grid(True)

axis.set_xlabel("t")
fig.suptitle("Convolution de fonctions rectangles", fontweight="bold")
fig.canvas.draw()
plt.show()
