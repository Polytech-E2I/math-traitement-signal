import control
import matplotlib.pyplot as plt

Tz = control.TransferFunction([1, -1], [1, 0])
control.pzmap(Tz, plot=True)

circ = plt.Circle([0, 0], radius=1, fill=False)

fig = plt.gcf()
ax = plt.gca()

ax.add_patch(circ)

plt.show()