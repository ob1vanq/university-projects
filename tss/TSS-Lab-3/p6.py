import numpy as np
from scipy import signal
from p1 import a, b, c1, c2
import matplotlib.pyplot as plt

func = signal.TransferFunction(b, a, dt=1)
t, y = signal.dimpulse(func, n=30)
fig, ax = plt.subplots()
plt.stem(np.squeeze(y), linefmt=c1, basefmt=c2)
ax.grid(linestyle="--")
ax.set(xlabel="t, с", ylabel="амплітуда")
fig.savefig("data/point 6.png")
plt.show()
plt.close()