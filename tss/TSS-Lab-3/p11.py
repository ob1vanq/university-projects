import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from p1 import a, b, c1, c2


t = np.linspace(0, 1, 256)
sq = signal.square(2*np.pi*10*t, 0.3)
y = signal.lfilter(b, a, x=sq)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t, sq, c1)
ax2.plot(t, y, c2)
for axis in (ax1, ax2):
    axis.grid(linestyle="--")
    axis.set(xlabel=f"t, с", ylabel="амплітуда")
plt.show()
plt.close()


