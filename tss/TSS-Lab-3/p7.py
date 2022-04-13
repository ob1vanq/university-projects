# 7. Розрахувати реакцію системи на сигнал з п. 2.1 з використанням функції розрахунку
# згортки convolve. Побудувати графіки вхідного та вихідного сигналу, аналогічні п. 2.1 (з
# нульовими початковими умовами). Всі отримані в п. 7 результати порівняти з п 2.1. Зробити
# висновки.
import numpy as np

from p2 import y as sig, c1
from p5 import y as win
from scipy import signal
import matplotlib.pyplot as plt

filtered = signal.convolve(sig, win)

sec = round(len(filtered)/256, 3)
t = np.linspace(0, sec, len(filtered))

fig, ax = plt.subplots()
ax.plot(t, filtered, c1)
ax.grid(linestyle="--")
ax.set(xlabel=f"t, с {sec =}", ylabel="амплітуда")
fig.savefig("data/point 7.png")
plt.show()
plt.close()


