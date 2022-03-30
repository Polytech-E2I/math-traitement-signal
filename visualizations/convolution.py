import numpy as np
import matplotlib.pyplot as plt
import sys

def plot_convolve(t, f1, f2, xmin=-5, xmax=50):
    """
    Uses numpy and matplotlib to display the convolution of f1 and f2
    """

    if (len(t) + len(f1) + len(f2)) != (3 * len(t)):
        sys.stderr.write("ERROR : t, f1 and f2 should have the same length")
        return

    T = t[1] - t[0] # sampling width

    # times T to scale the convolution
    conv = np.convolve(f1, f2, mode='same') * T

    fig, axis = plt.subplots(1, 1)

    axis.plot(t, f1, label=r'$f_1(t)$')
    axis.plot(t, f2, label=r'$f_2(t)$')
    axis.plot(t, conv, label=r'$f_1(t) * f_2(t)$')

    axis.legend(loc="best")
    axis.grid(True)

    axis.set_xlabel("temps")
    fig.suptitle("Convolution de $f_1$ et $f_2$", fontweight="bold")
    plt.xlim([xmin, xmax])

    fig.canvas.draw()
    plt.show()




n = 5000
t = np.linspace(-500, 500, n)

###
echelon = np.where(t >= 0, 1, 0)
####
T1 = 8
T2 = 2
rect1 = np.where(np.logical_and(t >= -T1/2, t <= T1/2), 1, 0)
rect2 = np.where(np.logical_and(t >= -T2/2, t <= T2/2), 1, 0)
####
Tsin = np.where(np.logical_and(t >= -80, t <= 80), 10, 20)
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

plot_convolve(t, rect1, rect2, -10, 10)
#plot_convolve(t, sinus, rectsinus, -200, 200)
#plot_convolve(t, expin, expc)