import numpy as np

from p1 import a, b, c1, c2
from scipy import signal
import matplotlib.pyplot as plt

w, h = signal.freqz(b, a, worN=100, fs=256)
fig, ax = plt.subplots()
ax.plot(w, h,  c1)
ax.grid(linestyle="--")
ax.set(xlabel=f"Частота, рад/с", ylabel="КЧХ")
fig.savefig("data/point 8.png")
plt.show()
