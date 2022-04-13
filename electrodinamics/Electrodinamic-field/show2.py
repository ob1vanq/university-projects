import numpy as np

from potentials import row, col, k
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12,6))

linewidth= 1
major_ticks = np.linspace(0, col, col+1)
minor_ticks = np.linspace(0, row, row+1)
с = "black"
c2 = "royalblue"
ax.plot([i+1 for i in range(col)], [1 for i in range(col)], color=с, linewidth=linewidth)
ax.plot([i+1 for i in range(col)], [row for i in range(col)], color=с, linewidth=linewidth)
ax.plot([1 for i in range(row)], [i+1 for i in range(row)], color=с, linewidth=linewidth)
ax.plot([col for i in range(row)], [i+1 for i in range(row)], color=с, linewidth=linewidth)
for i in range(row):
    for j in range(col):
        ax.scatter(j+1, i+1, color=c2, s=10)
indx = [i+1 for i in range(col)]
ax.plot(indx[1 * k:2 * k], [k for i in range(len(indx[1 * k:2 * k]))], color=с, linewidth=linewidth)
ax.plot(indx[4 * k:5 * k], [k for i in range(len(indx[4 * k:5 * k]))], color=с, linewidth=linewidth)
ax.set_xticks(major_ticks)
ax.set_yticks(minor_ticks)
ax.set(xlabel="Вісь j", ylabel="Вісь i", title=f"Сітка {row}x{col}")
plt.show()