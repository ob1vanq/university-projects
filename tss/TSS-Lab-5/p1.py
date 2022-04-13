
from params import plot, win
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 1)
axs[0].plot(win.parzen(100))
axs[1].plot(win.triang(100))
plot.set_param(axs)
fig.savefig("data/1.png")

