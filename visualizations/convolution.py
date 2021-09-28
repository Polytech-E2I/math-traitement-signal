import numpy as np
import matplotlib.pyplot as plt

T1 = 8
T2 = 2

n = 1000
xmin = -5
xmax = 50
t = np.linspace(-100, 100, n)
T = t[1] - t[0] # sampling width

echelon = np.where(t >= 0, 1, 0)

####
rect1 = np.where(np.logical_and(t >= -T1/2, t <= T1/2), 1, 0)
rect2 = np.where(np.logical_and(t >= -T2/2, t <= T2/2), 1, 0)
####
Tsin = np.where(np.logical_and(t >= -70, t <= 70), 10, 20)
sinus = np.sin((2*np.pi/Tsin) * t)
theta = 10
rectsinus = (1/theta) * np.where(np.logical_and(t >= -theta/2, t <= theta/2), 1, 0)
####
tau = 5
taup = 7
expin = (1/tau) * np.exp(-t/tau) * echelon
expc = (1/taup) * np.exp(-t/taup) * echelon
convolution_manuelle = (1/(tau-taup)) * (np.exp(-t/tau) - np.exp(-t/taup)) * echelon
####

f1 = expin
f2 = expc

conv = np.convolve(f1, f2, mode='same') * T # *T to scale the convolution

fig, axis = plt.subplots(1, 1)
axis.plot(t, f1, label=r'$f_1(t)$')# = \Pi(\frac{t}{T_1})$')
axis.plot(t, f2, label=r'$f_2(t)$')# = \Pi(\frac{t}{T_2})$')
axis.plot(t, conv, label=r'$f_1(t) * f_2(t)$')
axis.legend(loc="best")
axis.grid(True)

axis.set_xlabel("t")
fig.suptitle("Convolution de $f_1$ et $f_2$", fontweight="bold")
fig.canvas.draw()
plt.xlim([xmin, xmax])
plt.show()
