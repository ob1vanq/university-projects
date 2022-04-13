import numpy as np
import random
import matplotlib.pyplot as plt
from scipy import signal
from p1 import a, b, c1, c2


t = np.linspace(0, 1, 256)
y = np.sin(2 * np.pi * 10 * t)

z_null, _ = signal.lfilter(b, a, y, zi=[0 for i in range(5)])
z_rand, _ = signal.lfilter(b, a, y, zi=[random.random() for i in range(5)])

sec = int(0.1 * 256)
fig, ax = plt.subplots(2, 2, figsize=(14, 6))

ax[0, 0].plot(t, y, label="вхідний", color=c1)
ax[0, 0].plot(t, z_null, label="вихідний", color=c2)
ax[0, 1].plot(t[:sec], y[:sec], label="вхідний", color=c1)
ax[0, 1].plot(t[:sec], z_null[:sec], label="вихідний", color=c2)

ax[1, 0].plot(t, y, label="вхідний", color=c1)
ax[1, 0].plot(t, z_rand, label="вихідний", color=c2)
ax[1, 1].plot(t[:sec], y[:sec], label="вхідний", color=c1)
ax[1, 1].plot(t[:sec], z_rand[:sec], label="вихідний", color=c2)

title = ["Нульові початкові умови"] * 2 + ["Випадкові початкові умови"] * 2
i = 0
for axis in ax.flat:
    axis.grid(linestyle="--")
    axis.set(xlabel="t, с", ylabel="амплітуда")
    axis.legend(loc='upper right', title=title[i], shadow=True)
    i += 1

plt.tight_layout()
fig.savefig("data/point 2.png")
plt.show()
plt.close()
