import numpy as np
import matplotlib.pyplot as plt
from scipy import fft


Fe = 100 # Hz
duree = 10 # secondes

t = np.arange(1/Fe, duree, 1/Fe)
print(f"{t=}")

f0 = 20 # Hz
m = np.cos(2*np.pi*f0*t)

T = 0.25 # secondes
D = 2 # secondes

x = np.zeros(t.size)
for i in range(0, int(duree/D - T) + 1):
    x[int(i*Fe*D+1) : int(i*Fe*D+T*Fe)+1] = 1

print(f"{x=}")

s = m*x

fig, (ax1, ax2, ax3) = plt.subplots(3,1)

ax1.plot(t, m)
ax1.set_ylabel("figure 1a")

ax2.plot(t, x)
ax2.set_ylabel("figure 1b")

ax3.plot(t, s)
ax3.set_ylabel("figure 1c")

fig.suptitle("Figure 1")
plt.show()

M = 4096
S = fft.fft(s, M)

f = np.arange(0, M) / M * Fe

plt.plot(f, np.abs(S))
plt.title("Figure 2a")
plt.show()
