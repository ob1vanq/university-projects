from scipy import signal
from p1 import a, b, c1, c2
import matplotlib.pyplot as plt

h = signal.unit_impulse(30, 0)
y = signal.lfilter(b, a, x=h)
fig, ax = plt.subplots()
ax.stem(y, linefmt=c1, basefmt=c2)
ax.grid(linestyle="--")
fig.savefig("data/point 5.png")
plt.show()
plt.close()